import sys

import mysql.connector
from dotenv import load_dotenv

load_dotenv()
import os

# host = os.environ.get("MYSQL_HOST")
# port = int(os.environ.get("MYSQL_PORT"))
# user = os.environ.get("MYSQL_USER")
# passwd = os.environ.get("MYSQL_PASSWORD")
# dbName = os.environ.get("MYSQL_DATABASE")

host = "localhost"
port = 3306
user = "my_user"
passwd = "some_password_123"
dbName = "the_database"

mydb = mysql.connector.connect(host=host, port=port, user=user, passwd=passwd, db=dbName)


def executeFile(file):
    with open(os.path.join(sys.path[0], file), "r") as f:
        query = f.read()

    cursor = mydb.cursor(buffered=True)
    results = cursor.execute(query, multi=True)

    for cur in results:
        print('cursor:', cur)
        if cur.with_rows:
            print('result:', cur.fetchall())


executeFile("tables")
executeFile("inserts")

mydb.commit()
mydb.close()
