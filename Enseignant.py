class Enseignant:

    def __init__(self, uid: int):
        self.uid = uid

    def __str__(self):
        return f"Enseignant: {self.uid}"

    #Méthodes d'opérations CRUD

    def add_enseignant_bdd(self, conn):
            
            cur = conn.cursor()
            cur.execute(f"INSERT INTO enseignant (uid) VALUES ('{self.uid}')")
            conn.commit()
            cur.close()

    def update_enseignant_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE enseignant SET uid = '{self.uid}' WHERE Id_enseignant = {id}")
        conn.commit()
        cur.close()

    def delete_enseignant_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM enseignant WHERE Id_enseignant = {id}")
        conn.commit()
        cur.close()

    def get_enseignant_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM enseignant WHERE Id_enseignant = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    def get_all_enseignant_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM enseignant")
        rows = cur.fetchall()
        cur.close()
        return rows
    