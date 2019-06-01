from mysql.connector import (connection)
from flaskext.mysql import MySQL
import os
cnx = None
cursor = None
cnx = connection.MySQLConnection(user= os.environ.get('USER_NAME'), password=os.environ.get('PASSWORD'), 
                                     host='127.0.0.1',
                                     database='fruitstore')
cursor = cnx.cursor()
def close_connection():
    cursor.close()
    cnx.close()