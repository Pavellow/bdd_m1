class Inscription:
    def __init__(self, id_etape, id_etudiant, annee):
        self.id_etape = id_etape
        self.id_etudiant = id_etudiant
        self.annee = annee

    def __str__(self):
        return f"Inscription: {self.id_etape}, {self.id_etudiant}, {self.annee}"
    
    def add_inscription_bdd(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO inscription (id_etape, id_etudiant, annee) VALUES (%s, %s, %s)", 
                    (self.id_etape, self.id_etudiant, self.annee))
        conn.commit()
        cur.close()
    
    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete = "INSERT INTO inscription (id_etape, id_etudiant, annee) VALUES (%s, %s, %s)" % (self.id_etape, self.id_etudiant, self.annee)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")