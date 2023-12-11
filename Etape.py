class Etape:

    def __init__(self, id_diplome, Nom_filiere, Niveau, reponsable):
        self.id_diplome = id_diplome
        self.Nom_filiere = Nom_filiere
        self.Niveau = Niveau
        self.responsable = reponsable

    def __str__(self):
        return f"Etape: {self.id_diplome}, {self.Nom_filiere}, {self.Niveau}, {self.responsable}"

    #Méthodes d'opérations CRUD

    def add_etape_bdd(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO etape (id_diplome, Nom_etape, Niveau, responsable) VALUES (%s, %s, %s, %s)", 
                    (self.id_diplome, self.Nom_filiere, self.Niveau, self.responsable))
        conn.commit()
        cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete = "INSERT INTO etape (Nom_filiere, Niveau) VALUES (%s, %s)" % (self.Nom_filiere, self.Niveau)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")

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
        