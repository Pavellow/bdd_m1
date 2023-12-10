class Entreprise:

    def __init__(self, siret, nom_entreprise, adresse_entreprise):
        self.siret = siret
        self.nom_entreprise = nom_entreprise
        self.adresse_entreprise = adresse_entreprise

    def __str__(self):
        return f"Entreprise: {self.Nom}"
    
    # Getter pour le nom
    def get_nom(self):
        return self.nom_entreprise
    
    # Setter pour le nom    
    def set_nom(self, nom):
        self.nom_entreprise = nom

    #Méthodes d'opérations CRUD

    def add_entreprise_bdd(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO entreprise (siret, nom_entreprise, adresse_entreprise) VALUES (%s, %s, %s)", 
                    (self.siret, self.nom_entreprise, self.adresse_entreprise))
        conn.commit()
        cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete = "INSERT INTO entreprise (nom_entreprise) VALUES (%s)" % (self.Nom)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")