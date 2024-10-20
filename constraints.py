import logging
from sqlalchemy import create_engine, Index, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.schema import AddConstraint, CreateIndex
from create_tables import Base, User, Class, StudentClass, Transaction, db_url

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create the engine
engine = create_engine(db_url)

def add_indexes_and_constraints():
    try:
        with engine.begin() as connection:
            # Add index to download_code in classes table
            download_code_index = Index('ix_classes_download_code', Class.download_code)
            connection.execute(CreateIndex(download_code_index))
            logging.info("Added index on download_code in classes table")

            # Add indexes to student_id and class_id in student_classes table
            student_id_index = Index('ix_student_classes_student_id', StudentClass.student_id)
            class_id_index = Index('ix_student_classes_class_id', StudentClass.class_id)
            connection.execute(CreateIndex(student_id_index))
            connection.execute(CreateIndex(class_id_index))
            logging.info("Added indexes on student_id and class_id in student_classes table")

            # Add index to trade_date (timestamp) in transactions table
            trade_date_index = Index('ix_transactions_timestamp', Transaction.timestamp)
            connection.execute(CreateIndex(trade_date_index))
            logging.info("Added index on timestamp in transactions table")

            # Add uniqueness constraint on download_code in classes table
            unique_download_code = UniqueConstraint(Class.download_code, name='uq_classes_download_code')
            connection.execute(AddConstraint(unique_download_code))
            logging.info("Added uniqueness constraint on download_code in classes table")

            # Add foreign key constraints (if not already present)
            # Note: These should already be defined in the model, but we'll add them here for completeness
            fk_student_classes_student = ForeignKeyConstraint([StudentClass.student_id], [User.id], ondelete='CASCADE')
            fk_student_classes_class = ForeignKeyConstraint([StudentClass.class_id], [Class.id], ondelete='CASCADE')
            fk_transactions_student = ForeignKeyConstraint([Transaction.student_id], [User.id], ondelete='CASCADE')

            connection.execute(AddConstraint(fk_student_classes_student))
            connection.execute(AddConstraint(fk_student_classes_class))
            connection.execute(AddConstraint(fk_transactions_student))
            logging.info("Added foreign key constraints for referential integrity")

        logging.info("Successfully added all indexes and constraints")
    except Exception as error:
        logging.error(f"Error adding indexes and constraints: {error}")

if __name__ == '__main__':
    logging.info("Starting to add indexes and constraints")
    add_indexes_and_constraints()
    logging.info("Process completed")

