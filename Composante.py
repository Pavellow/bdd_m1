class Composante:
    
    def __init__(self, libelle, id_composante):
        self.Libelle_composante = libelle
        self.id_composante = id_composante

    def __str__(self):
        return f"Composante: {self.Libelle_composante}"
    
    def to_string(self):
        return f"Composante: {self.Libelle_composante} | id: {self.id_composante}"
    
    def set_libelle(self, libelle_param):
        self.Libelle_composante = libelle_param

    def set_id(self, id_param):
        self.id_composante = id_param

    
    #Méthodes d'opérations CRUD

    def add_composante_bdd(self, conn):
        """ajoute une composante dans la base de données

        Args:
            conn (pymsql): connexion à la base de données
            """
        cur = conn.cursor()
        cur.execute("INSERT INTO composante (Libelle_composante, id_composante) VALUES (%s, %s)", 
                    (self.Libelle_composante, self.id_composante))
        conn.commit()
        cur.close()

    def ecrire_requete_dans_fichier(self, nom_fichier):
        """écriture d'un requête dans un fichier

        Args:
            nom_fichier (str): nom du fichier sql
        """
        requete = "INSERT INTO composante (Libelle_composante, id_composante) VALUES (%s, %s)" % (self.Libelle_composante, self.id_composante)
        with open(nom_fichier, "a") as fichier:
            fichier.write(requete + "\n\n")

    def update_composante_libelle_bdd(self, conn, id):
        """modificiation du libelle d'une composante dans la base de données

        Args:
            conn (pymysql): connexion à la base de données
            id (int): id de la composante
        """
        cur = conn.cursor()
        cur.execute(f"UPDATE composante SET Libelle_composante = {self.Libelle_composante} WHERE Id_composante = {id}")
        conn.commit()
        cur.close()

    def update_composante_id_bdd(self, conn, id):
        """modificiation de l'id d'une composante dans la base de données

        Args:
            conn (pymysql): connexion à la base de données
            id (int): id de la composante
        """
        cur = conn.cursor()
        cur.execute(f"UPDATE composante SET id_composante = '{self.id_composante}' WHERE Id_composante = {id}")
        conn.commit()
        cur.close()

    def delete_composante_bdd(self, conn, id):
        """suppression d'une composante dans la base de données

        Args:
            conn (pymysql): connexion à la base de données
            id (int): id de la composante
        """
        cur = conn.cursor()
        cur.execute(f"DELETE FROM composante WHERE Id_composante = {id}")
        conn.commit()
        cur.close()

    def get_composante_bdd(self, conn, id):
        """lire la composante dans la base de données

        Args:
            conn (pymysql): connexion à la base de données
            id (int): id de la composante

        Returns:
            tuple: ligne de la composante
        """
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM composante WHERE Id_composante = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_all_composante_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM composante")
        rows = cur.fetchall()
        cur.close()
        return rows

        