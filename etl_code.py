import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


# value to connect server
server="{server_name}"
database="{database}"
driver="{driver}"
 
# create engine
engine = create_engine('mssql+pyodbc://@' + '{server_name}' + '/' + '{database_name}' + '?trusted_connection=yes&driver={driver}')

# test connection
try:
    engine.connect() 
    print("success")
except SQLAlchemyError as err:
    print("error", err.__cause__) 

# read sql
with engine.connect() as conn:
   df = pd.read_sql_query('query', conn)

df.to_csv('file_name')
