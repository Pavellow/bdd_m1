class Etudiant:

    def __init__(self, id_filiere, uid):
        self.id_filiere = id_filiere
        self.uid = uid

    def __str__(self):
        return f"Etudiant: {self.id_filiere}, {self.uid}"

    #Méthodes d'opérations CRUD

    def add_etudiant_bdd(self, conn):               
        cur = conn.cursor()
        cur.execute(f"INSERT INTO etudiant (id_filiere, uid) VALUES (%s, %s)", (self.id_filiere, self.uid))
        conn.commit()
        cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete =f"INSERT INTO etudiant (id_filiere, uid) VALUES (%s, %s)" % (self.id_filiere, self.uid)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")

    def update_etudiant_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE etudiant SET id_filiere = '{self.id_filiere}', uid = '{self.uid}' WHERE Id_etudiant = {id}")
        conn.commit()
        cur.close()

    def delete_etudiant_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM etudiant WHERE Id_etudiant = {id}")
        conn.commit()
        cur.close()

    def get_etudiant_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM etudiant WHERE Id_etudiant = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_all_etudiant_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM etudiant")
        rows = cur.fetchall()
        cur.close()
        return rows