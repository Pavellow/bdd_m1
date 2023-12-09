import pymysql

class SQLConn:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password= password
        self.database = database
    
    def connect_to_bdd(self):
        self.conn = pymysql.connect(host=self.host, user=self.user,password=self.password, database=self.database)
        return self.conn

    def close_connection(self):
        self.conn.close()
        self.cursor.close()