class Tuteur:
    def __init__(self, Nom_tuteur, id_entreprise):
        self.Nom_tuteur = Nom_tuteur
        self.id_entreprise = id_entreprise

    def __str__(self):
        return f"Tuteur: {self.Nom_tuteur}, {self.id_entreprise}"

    #Méthodes d'opérations CRUD

    def add_tuteur_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO tuteur (Nom_tuteur, id_entreprise) VALUES (%s, %s)", (self.Nom_tuteur, self.id_entreprise))
        conn.commit()
        cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete = f"INSERT INTO tuteur (Nom_tuteur, id_entreprise) VALUES (%s, %s)" % (self.Nom_tuteur, self.id_entreprise)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")

    def update_tuteur_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE tuteur SET Nom_tuteur = '{self.Nom_tuteur}', id_entreprise = '{self.id_entreprise}' WHERE Id_tuteur = {id}")
        conn.commit()
        cur.close()

    def delete_tuteur_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM tuteur WHERE Id_tuteur = {id}")
        conn.commit()
        cur.close()

    def get_tuteur_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM tuteur WHERE Id_tuteur = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows