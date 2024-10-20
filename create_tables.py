from sqlalchemy import create_engine, Column, String, Numeric, DateTime, Enum, ForeignKey, Table, MetaData, inspect, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func

# Python 3.13 compatible version (commented out):
# from sqlalchemy.engine.url import make_url
# db_url = "postgresql://postgres:postgres@localhost:5432/postgres"
# url = make_url(db_url)
# url = url.set(drivername='postgresql+pg8000')
# engine = create_engine(url)

# Python 3.12 or lower compatible version:
db_url = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(db_url)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define User model based on existing table
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(UUID(as_uuid=True), primary_key=True)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    roles = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    avatarId = Column(UUID(as_uuid=True))

# Define the other models
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    district = Column(String)
    school = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class Class(Base):
    __tablename__ = 'classes'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    teacher_id = Column(UUID(as_uuid=True), ForeignKey('teachers.id', ondelete='CASCADE'))
    name = Column(String, nullable=False)
    download_code = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class StudentClass(Base):
    __tablename__ = 'student_classes'

    student_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    class_id = Column(UUID(as_uuid=True), ForeignKey('classes.id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    student = relationship("User", foreign_keys=[student_id])

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    student_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    stock_id = Column(String, nullable=False)
    type = Column(Enum('buy', 'sell', name='transaction_type'), nullable=False)
    quantity = Column(Numeric, nullable=False)
    price = Column(Numeric, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())

    student = relationship("User", foreign_keys=[student_id])

def create_tables():
    try:
        # Create all tables in the engine, except for 'users' which already exists
        Base.metadata.create_all(engine, tables=[t for t in Base.metadata.tables.values() if t.name != 'users'])
        print("Tables created successfully!")
    except Exception as error:
        print(f"Error: {error}")

def inspect_database():
    inspector = inspect(engine)
    
    # Print current database and schema
    with engine.connect() as connection:
        current_db = connection.execute(text("SELECT current_database()")).scalar()
        current_schema = connection.execute(text("SELECT current_schema()")).scalar()
        print(f"Current Database: {current_db}")
        print(f"Current Schema: {current_schema}")
    
    # Get list of table names
    table_names = inspector.get_table_names()
    print("Tables in the database:")
    for table_name in table_names:
        print(f"- {table_name}")
        
        # Get columns for each table
        columns = inspector.get_columns(table_name)
        print("  Columns:")
        for column in columns:
            print(f"    - {column['name']} ({column['type']})")
        
        # Get foreign keys for each table
        foreign_keys = inspector.get_foreign_keys(table_name)
        if foreign_keys:
            print("  Foreign Keys:")
            for fk in foreign_keys:
                print(f"    - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")
        
        print()  # Empty line for readability

if __name__ == '__main__':
    create_tables()
    
    # Create a session and commit the transaction
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.commit()
    
    inspect_database()
