import logging
from sqlalchemy import create_engine, inspect, text, Boolean, String, Column
from sqlalchemy.orm import sessionmaker
from create_tables import Base, User, db_url

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create the engine
engine = create_engine(db_url)

def modify_users_table():
    try:
        with engine.connect() as connection:
            # Check if columns already exist
            inspector = inspect(engine)
            existing_columns = [col['name'] for col in inspector.get_columns('users')]

            if 'is_teacher' not in existing_columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN is_teacher BOOLEAN DEFAULT false"))
                logging.info("Added is_teacher column to users table")
            else:
                logging.info("is_teacher column already exists in users table")

            if 'last_initial' not in existing_columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN last_initial VARCHAR(1)"))
                logging.info("Added last_initial column to users table")
            else:
                logging.info("last_initial column already exists in users table")

            # Add first_name column regardless of firstName
            if 'first_name' not in existing_columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN first_name VARCHAR(255)"))
                logging.info("Added first_name column to users table")
            else:
                logging.info("first_name column already exists in users table")

            connection.commit()
        logging.info("Users table modified successfully")
    except Exception as error:
        logging.error(f"Error modifying users table: {error}")

def update_user_model():
    # Update the User model to reflect the changes
    if not hasattr(User, 'is_teacher'):
        User.is_teacher = Column(Boolean, default=False, nullable=False)
        logging.info("Added is_teacher attribute to User model")
    
    if not hasattr(User, 'last_initial'):
        User.last_initial = Column(String(1))
        logging.info("Added last_initial attribute to User model")

    if not hasattr(User, 'first_name'):
        User.first_name = Column(String(255))
        logging.info("Added first_name attribute to User model")

    logging.info("User model updated")

if __name__ == '__main__':
    logging.info("Starting table modification process")
    modify_users_table()
    update_user_model()
    
    # Create a session and commit the transaction
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.commit()
    logging.info("Session committed")
    
    # Inspect the updated table
    inspector = inspect(engine)
    columns = inspector.get_columns('users')
    logging.info("Updated users table columns:")
    for column in columns:
        logging.info(f"- {column['name']} ({column['type']})")

    logging.info("Table modification process completed")
