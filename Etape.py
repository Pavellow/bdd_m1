class Etape:

    def __init__(self, Nom_filiere, Niveau):
        self.Nom_filiere = Nom_filiere
        self.Niveau = Niveau

    def __str__(self):
        return f"Etape: {self.Nom_filiere}, {self.Niveau}"

    #Méthodes d'opérations CRUD

    def add_etape_bdd(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO etape (Nom_filiere, Niveau) VALUES (%s, %s)", 
                    (self.Nom_filiere, self.Niveau))
        conn.commit()
        cur.close()


    def update_etape_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE etape SET Nom_filiere = '{self.Nom_filiere}', Niveau = '{self.Niveau}' WHERE Id_etape = {id}")
        conn.commit()
        cur.close()
    
    def delete_etape_bdd(self, conn, id):
    
        cur = conn.cursor()
        cur.execute(f"DELETE FROM etape WHERE Id_etape = {id}")
        conn.commit()
        cur.close()

    def get_etape_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM etape WHERE Id_etape = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    def get_all_etape_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM etape")
        rows = cur.fetchall()
        cur.close()
        return rows
        