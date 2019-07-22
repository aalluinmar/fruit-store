from mysql.connector import (connection)
from flaskext.mysql import MySQL
import os
cnx = None
cursor = None


class DB(object):
    def __init__(self):
        cnx = connection.MySQLConnection(user=os.environ.get('USER_NAME'), password=os.environ.get('PASSWORD'),
                                         host='127.0.0.1',
                                         database='nodejs_login1')
        self.cursor = cnx.cursor()
        self.cnx = cnx

    def get_rows(self, statement):
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        return rows

    def query_insert(self, statement):
        self.cursor.execute(statement)
        self.cnx.commit()

    def close_connection(self):
        self.cursor.close()
        self.cnx.close()
