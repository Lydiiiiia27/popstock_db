import logging
from sqlalchemy import create_engine, Index, UniqueConstraint, ForeignKeyConstraint, Column, String
from sqlalchemy.schema import AddConstraint, CreateIndex
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine.url import make_url

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the database URL
db_url = "postgresql://postgres:postgres@localhost:5432/postgres"

# Python 3.13 compatible version (commented out):
# from sqlalchemy.engine.url import make_url
# url = make_url(db_url)
# url = url.set(drivername='postgresql+pg8000')
# engine = create_engine(url)

# Python 3.12 or lower compatible version:
engine = create_engine(db_url)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define minimal models for constraint creation
class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(String, primary_key=True)
    download_code = Column(String)

class StudentClass(Base):
    __tablename__ = 'student_classes'
    student_id = Column(String, primary_key=True)
    class_id = Column(String, primary_key=True)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(String, primary_key=True)
    student_id = Column(String)
    timestamp = Column(String)

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

            # Add foreign key constraints
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
