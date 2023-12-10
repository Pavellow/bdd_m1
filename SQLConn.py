import pymysql

class SQLConn:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password= password
        self.database = database
    
    def connect_to_bdd(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        return self.conn

    def close_connection(self):
        self.conn.close()

    def delete_row(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        conn = self.connect_to_bdd()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        self.close_connection()

    def update_row(self, table, set_clause, set_params, condition_clause, condition_params):
        query = f"UPDATE {table} SET {set_clause} WHERE {condition_clause}"
        params = set_params + condition_params
        conn = self.connect_to_bdd()
    
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
        except Exception as e:
            print(f"Une erreur est survenue lors de la mise à jour : {e}")
            conn.rollback()
        finally:
            self.close_connection(conn)



    def add_row(self, table, values):
        query = f"INSERT INTO {table} VALUES ({values})"
        self.conn = self.connect_to_bdd()
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
        self.close_connection()