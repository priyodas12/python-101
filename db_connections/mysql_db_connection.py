from datetime import datetime

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

my_sql_db_host=os.environ['MYSQL_DB_HOST']
my_sql_db_username=os.environ['MYSQL_DB_USER']
my_sql_db_password=os.environ['MYSQL_DB_PASS']
my_sql_db=os.environ['MYSQL_DB']

connection=mysql.connector.connect(
    host=my_sql_db_host,
    user=my_sql_db_username,
    password=my_sql_db_password ,
    database=my_sql_db
)

cursor=connection.cursor()
print(f"connected to MySQL database {my_sql_db} at {datetime.now()}")
cursor.execute(
     "SELECT * FROM orders"
)
for row in cursor.fetchall():
    print(f"\n{row}")
connection.close()



