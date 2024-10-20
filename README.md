# Database Table Creation and Modification Scripts

## Author
Lydia

## Description
This project contains two Python scripts:
1. `create_tables.py`: Creates database tables for a popstock teacher website using SQLAlchemy ORM.
2. `modify.py`: Modifies the existing `users` table to add new columns and update the User model.

Both scripts connect to a local PostgreSQL database and work with the necessary tables based on defined models.

## Components
### create_tables.py
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

### modify.py
1. Database Connection Setup
2. User Table Modification Function
3. User Model Update Function
4. Main Execution Block

## Prerequisites
- Python 3.x
- SQLAlchemy
- PostgreSQL

## Database Configuration
Both scripts are configured to connect to a local PostgreSQL database with the following details:
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
2. Run the create_tables.py script:
   ```
   python create_tables.py
   ```
3. Run the modify.py script:
   ```
   python modify.py
   ```

## Functionality
### create_tables.py
- Creates the defined tables in your local PostgreSQL database.
- Skips creating the 'users' table, assuming it already exists.
- Inspects the database and prints out the structure of all tables, including columns and foreign key relationships.

### modify.py
- Modifies the existing 'users' table to add new columns:
  - `is_teacher` (BOOLEAN)
  - `last_initial` (VARCHAR(1))
  - `first_name` (VARCHAR(255))
- Updates the User model to reflect these changes.
- Logs the modification process and the updated table structure.

## Note
- Make sure your local PostgreSQL database is running before executing the scripts.
- The scripts use a 10-second connection timeout.
- If you encounter any issues, check your database credentials and ensure PostgreSQL is running and accessible.

## Troubleshooting
If you encounter any errors, they will be printed to the console. Common issues might include:
- Database connection problems
- Insufficient permissions
- Conflicting table names or column names

For any persistent issues, please check your PostgreSQL configuration and ensure you have the necessary permissions to create and modify tables in the specified database.

## Logging
The `modify.py` script includes logging functionality. You can find detailed logs of the modification process in the console output when running the script.
