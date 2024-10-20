# PopStock Database Management

This project contains scripts for managing and modifying the PopStock database schema.

## Requirements

- Python 3.12 or lower (3.13 support is commented out but available)
- PostgreSQL database

## Installation

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source .venv/bin/activate
     ```

3. Install the required packages:
   ```
   pip install sqlalchemy psycopg2-binary
   ```

## Configuration

Important: Update the `db_url` in each script (`create_tables.py`, `modify.py`, and `constraints.py`) to match your PostgreSQL database configuration:

```python
db_url = "postgresql://username:password@host:port/database_name"
```

Make sure to replace `username`, `password`, `host`, `port`, and `database_name` with your actual PostgreSQL connection details.

## Usage

1. Create tables:
   ```
   python create_tables.py
   ```

2. Modify users table:
   ```
   python modify.py
   ```

3. Add constraints and indexes:
   ```
   python constraints.py
   ```

## File Descriptions

- `create_tables.py`: Creates the initial database schema.
- `modify.py`: Adds new columns to the users table.
- `constraints.py`: Adds indexes and constraints to the database.

## Notes

- The scripts are currently set up for Python 3.12 and lower.
- For Python 3.13 support, uncomment the relevant sections in each file and install `pg8000` instead of `psycopg2-binary`:
  ```
  pip install pg8000
  ```

## Troubleshooting

If you encounter any issues:
1. Ensure your PostgreSQL server is running and accessible.
2. Double-check that the database URL in each script matches your PostgreSQL setup.
3. Verify that you have the necessary permissions to modify the database.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
