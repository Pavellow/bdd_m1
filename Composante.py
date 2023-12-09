class Composante:
    
    def __init__(self, libelle):
        self.Libelle_composante = libelle

    def __str__(self):
        return f"Composante: {self.Libelle_composante}"
    
    #Méthodes d'opérations CRUD

    def add_composante_bdd(self, conn):
        
        cur = conn.cursor()
        cur.execute(f"INSERT INTO composante (Libelle_composante) VALUES ('{self.Libelle_composante}')")
        conn.commit()
        cur.close()

    def update_composante_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE composante SET Libelle_composante = '{self.Libelle_composante}' WHERE Id_composante = {id}")
        conn.commit()
        cur.close()

    def delete_composante_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM composante WHERE Id_composante = {id}")
        conn.commit()
        cur.close()

    def get_composante_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM composante WHERE Id_composante = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_all_composante_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM composante")
        rows = cur.fetchall()
        cur.close()
        return rows

        