# SQL Server to CSV Exporter

This Python script utilizes the SQLAlchemy and Pandas libraries to export tables from a Microsoft SQL Server database to CSV files.

## Prerequisites

- Python 3.x installed
- Required Python libraries: SQLAlchemy, pandas, pyodbc (installed automatically with SQLAlchemy)

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python libraries using pip:
    ```
    pip install sqlalchemy pandas
    ```
3. Ensure you have appropriate access rights and network connectivity to connect to the SQL Server.

## Usage

1. Open the `sql_to_csv_export.py` file.
2. Modify the following variables according to your SQL Server setup:
    - `server`: Name or IP address of the SQL Server.
    - `database`: Name of the database to connect to.
    - `driver`: ODBC driver name for SQL Server (e.g., `ODBC Driver 17 for SQL Server`).
3. Replace `'query'` in `pd.read_sql_query('query', conn)` with your SQL query to retrieve the desired data.
4. Run the script using Python:
    ```
    python sql_to_csv_export.py
    ```
5. The script will connect to the SQL Server, execute the provided SQL query, and export the resulting data to a CSV file named `file_name.csv`.
