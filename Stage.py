class Stage:
    
    def __init__(self, id_etudiant, id_entreprise, id_tuteur, feedback_stage, feedback_entreprise, feedback_prof, etat):
        self.id_etudiant = id_etudiant
        self.id_entreprise = id_entreprise
        self.id_tuteur = id_tuteur
        self.feedback_stage = feedback_stage
        self.feedback_entreprise = feedback_entreprise
        self.feedback_prof = feedback_prof
        self.etat = etat

    def __str__(self):
        return f"Stage: {self.id_etudiant}, {self.id_entreprise}, {self.id_tuteur}, {self.feedback_stage}, {self.feedback_entreprise}, {self.feedback_prof}, {self.etat}"

    #Méthodes d'opérations CRUD

    def add_stage_bdd(self, conn):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO stage (id_etudiant, id_entreprise, id_tuteur, feedback_stage, feedback_entreprise, feedback_prof, etat) VALUES ('{self.id_etudiant}', '{self.id_entreprise}', '{self.id_tuteur}', '{self.feedback_stage}', '{self.feedback_entreprise}', '{self.feedback_prof}', '{self.etat}')")
        conn.commit()
        cur.close()

    def update_stage_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"UPDATE stage SET id_etudiant = '{self.id_etudiant}', id_entreprise = '{self.id_entreprise}', id_tuteur = '{self.id_tuteur}', feedback_stage = '{self.feedback_stage}', feedback_entreprise = '{self.feedback_entreprise}', feedback_prof = '{self.feedback_prof}', etat = '{self.etat}' WHERE Id_stage = {id}")
        conn.commit()
        cur.close()

    def delete_stage_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"DELETE FROM stage WHERE Id_stage = {id}")
        conn.commit()
        cur.close()

    def get_stage_bdd(self, conn, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM stage WHERE Id_stage = {id}")
        rows = cur.fetchall()
        cur.close()
        return rows
