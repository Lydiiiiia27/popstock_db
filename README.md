# Database Table Creation Script

## Author
Lydia

## Description
This Python script (`create_tables.py`) is designed to create database tables for a popstock teacher website using SQLAlchemy ORM. It connects to a local PostgreSQL database and creates the necessary tables based on defined models.

## Components
The script consists of several main parts:

1. Database Connection Setup
2. Model Definitions
   - User
   - Teacher
   - Class
   - StudentClass
   - Transaction
3. Table Creation Function
4. Database Inspection Function
5. Main Execution Block

## Prerequisites
- Python 3.x
- SQLAlchemy
- PostgreSQL

## Database Configuration
The script is configured to connect to a local PostgreSQL database with the following details:
- Host: localhost
- Port: 5432
- Database: postgres
- Username: postgres
- Password: postgres

Ensure your local PostgreSQL instance is running and accessible with these credentials.

## Usage
1. Ensure you have the required dependencies installed:
   ```
   pip install sqlalchemy psycopg2-binary
   ```
2. Run the script:
   ```
   python create_tables.py
   ```

## Functionality
- The script will attempt to create the defined tables in your local PostgreSQL database.
- It will skip creating the 'users' table, assuming it already exists.
- After creating the tables, it will inspect the database and print out the structure of all tables, including columns and foreign key relationships.

## Note
- Make sure your local PostgreSQL database is running before executing the script.
- The script uses a 10-second connection timeout.
- If you encounter any issues, check your database credentials and ensure PostgreSQL is running and accessible.

## Troubleshooting
If you encounter any errors, they will be printed to the console. Common issues might include:
- Database connection problems
- Insufficient permissions
- Conflicting table names

For any persistent issues, please check your PostgreSQL configuration and ensure you have the necessary permissions to create tables in the specified database.
