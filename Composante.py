class Composante:
    
    def __init__(self, libelle, id_composante):
        self.Libelle_composante = libelle
        self.id_composante = id_composante

    def __str__(self):
        return f"Composante: {self.Libelle_composante}"
    
    #Méthodes d'opérations CRUD

    def add_composante_bdd(self, conn):
        
        cur = conn.cursor()
        cur.execute(f"INSERT INTO composante (Libelle_composante, id_composante) VALUES ('{self.Libelle_composante}', '{self.id_composante}')")
        conn.commit()
        cur.close()

    def update_composante_libelle_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE composante SET Libelle_composante = '{self.Libelle_composante}' WHERE Id_composante = {id}")
        conn.commit()
        cur.close()

    def update_composante_id_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE composante SET id_composante = '{self.id_composante}' WHERE Id_composante = {id}")
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

        