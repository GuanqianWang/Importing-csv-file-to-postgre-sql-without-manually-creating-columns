import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('Your_dataset.csv')

# Define your connection parameters
username = 'postgres' # This is the default user name, use your username if defined otherwise
password = 'your password'
host = 'localhost'  # or your host
port = '5432'       # default port for PostgreSQL
database = 'your database name'

# Create a connection string
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string)

# Load the DataFrame into PostgreSQL
df.to_sql('Your data frame name', con=engine, if_exists='replace', index=False)

engine.dispose()
