class Compte:

    def __init__(self, password, Nom, Prenom):
        self.Password = password
        self.Nom = Nom
        self.Prenom = Prenom

    def __str__(self):
        return f"Compte: {self.Password}, {self.Nom}, {self.Prenom}"
     # Getter pour le mot de passe

    def get_password(self):
        return self.Password

    # Setter pour le mot de passe
    def set_password(self, password):
        self.Password = password

    # Getter pour le nom
    def get_nom(self):
        return self.Nom

    # Setter pour le nom
    def set_nom(self, nom):
        self.Nom = nom

    # Getter pour le prénom
    def get_prenom(self):
        return self.Prenom

    # Setter pour le prénom
    def set_prenom(self, prenom):
                self.Prenom = prenom
    #Méthodes d'opérations CRUD

    def add_compte_bdd(self, conn):
        cur = conn.cursor()
        cur.execute("INSERT INTO compte (Password, Nom, Prenom) VALUES (%s, %s, %s)", 
                    (self.Password, self.Nom, self.Prenom))
        conn.commit()
        cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        requete = "INSERT INTO compte (Password, Nom, Prenom) VALUES (%s, %s, %s)" % (self.Password, self.Nom, self.Prenom)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")
    
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

    