import pandas as pd
from sqlalchemy import create_engine

# # Sample DataFrame
# data = {
#     'column1': [1, 2, 3],
#     'column2': ['A', 'B', 'C']
# }
# df = pd.DataFrame(data)

df = pd.read_csv('US_only.csv')

# Define your connection parameters
username = 'postgres'
password = '8880323asdASD'
host = 'localhost'  # or your host
port = '5432'       # default port for PostgreSQL
database = 'fake_job_posting'

# Create a connection string
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string)

# Load the DataFrame into PostgreSQL
df.to_sql('US_only', con=engine, if_exists='replace', index=False)

engine.dispose()
