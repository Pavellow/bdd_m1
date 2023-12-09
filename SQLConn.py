import pymysql

class SQLConn:

    def __init__(self, host, user, password, database, conn):
        self.host = host
        self.user = user
        self.password= password
        self.database = database
    
    def connect(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.cursor.close()