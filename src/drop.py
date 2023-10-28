import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv


# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
import psycopg2

con = psycopg2.connect(host = "localhost",
    user = 'gitpod', 
    password = 'postgres',
    database = 'prueba',
)
cur = con.cursor()


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

cur.execute("""DROP TABLE publishers CASCADE""")
cur.execute("""DROP TABLE authors CASCADE""")
cur.execute("""DROP TABLE books CASCADE""")
cur.execute("""DROP TABLE book_authors CASCADE""")

con.commit()

cur.close()
con.close()