# Database Table Creation, Modification, and Constraint Scripts

## Author
Lydia

## Description
This project contains three Python scripts:
1. `create_tables.py`: Creates database tables for a popstock teacher website using SQLAlchemy ORM.
2. `modify.py`: Modifies the existing `users` table to add new columns and update the User model.
3. `constraints.py`: Adds indexes and constraints to the database tables.

All scripts connect to a local PostgreSQL database and work with the necessary tables based on defined models.

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

### constraints.py
1. Database Connection Setup
2. Table Existence Check and Creation Function
3. Index and Constraint Addition Function
4. Main Execution Block

## Prerequisites
- Python 3.x
- SQLAlchemy
- PostgreSQL

## Database Configuration
All scripts are configured to connect to a local PostgreSQL database with the following details:
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
4. Run the constraints.py script:
   ```
   python constraints.py
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

### constraints.py
- Checks if required tables exist and creates them if necessary.
- Adds the following indexes:
  - `download_code` in the `classes` table
  - `student_id` and `class_id` in the `student_classes` table
  - `timestamp` in the `transactions` table
- Adds a uniqueness constraint on `download_code` in the `classes` table
- Adds foreign key constraints for referential integrity
- Logs the entire process of adding indexes and constraints

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
The `modify.py` and `constraints.py` scripts include logging functionality. You can find detailed logs of the modification and constraint addition processes in the console output when running these scripts.
