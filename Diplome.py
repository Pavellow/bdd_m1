class Diplome:

    def __init__(self, Libelle_diplome, id_composante):
        self.Libelle_diplome = Libelle_diplome
        self.id_composante = id_composante

    def __str__(self):
        return f"Diplome: {self.Libelle_diplome}, {self.id_composante}"

    #Méthodes d'opérations CRUD

    def add_diplome_bdd(self, conn):
            
            cur = conn.cursor()
            cur.execute("INSERT INTO diplome (Libelle_diplome, id_composante) VALUES (%s, %s)", 
                    (self.Libelle_diplome, self.id_composante))
            conn.commit()
            cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete = "INSERT INTO diplome (Libelle_diplome, id_composante) VALUES (%s, %s)" % (self.Libelle_diplome, self.id_composante)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")

    def update_diplome_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE diplome SET Libelle_diplome = '{self.Libelle_diplome}', id_composante = '{self.id_composante}' WHERE Id_diplome = {id}")
        conn.commit()
        cur.close()

    def delete_diplome_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM diplome WHERE Id_diplome = {id}")
        conn.commit()
        cur.close()

    def get_diplome_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM diplome WHERE Id_diplome = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    def get_all_diplome_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM diplome")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    