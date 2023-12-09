class Entreprise:

    def __init__(self, nom):
        self.Nom = nom

    def __str__(self):
        return f"Entreprise: {self.Nom}"
    
    # Getter pour le nom
    def get_nom(self):
        return self.Nom
    
    # Setter pour le nom    
    def set_nom(self, nom):
        self.Nom = nom

    #Méthodes d'opérations CRUD

    def add_entreprise_bdd(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO entreprise (nom_entreprise) VALUES (%s)", 
                    (self.Nom))
        conn.commit()
        cur.close()