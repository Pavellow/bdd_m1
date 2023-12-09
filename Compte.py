class Compte:

    def __init__(self, password, Nom, Prenom):
        self.Password = password
        self.Nom = Nom
        self.Prenom = Prenom

    def __str__(self):
        return f"Compte: {self.Password}, {self.Nom}, {self.Prenom}"

    #Méthodes d'opérations CRUD

    def add_compte_bdd(self, conn):
        
        cur = conn.cursor()
        cur.execute(f"INSERT INTO compte (Password, Nom, Prenom) VALUES ('{self.Password}', '{self.Nom}', '{self.Prenom}')")
        conn.commit()
        cur.close()
    
    def update_compte_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE compte SET Password = '{self.Password}', Nom = '{self.Nom}', Prenom = '{self.Prenom}' WHERE Id_compte = {id}")
        conn.commit()
        cur.close()

    def delete_compte_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compte WHERE Id_compte = {id}")
        conn.commit()
        cur.close()

    def get_compte_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM compte WHERE Id_compte = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_all_compte_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM compte")
        rows = cur.fetchall()
        cur.close()
        return rows

    