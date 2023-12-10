

SELECT e.nom_entreprise, e.adresse_entreprise
FROM entreprise e
WHERE NOT EXISTS (
    SELECT 1
    FROM stage s
    WHERE s.id_entreprise = e.id_entreprise
    AND s.note < (SELECT AVG(note) FROM stage WHERE s.etat = "Terminé")
)

SELECT DISTINCT e.nom_entreprise, e.adresse_entreprise
FROM entreprise e
LEFT JOIN stage s ON e.id_entreprise = s.id_entreprise AND s.note < (SELECT AVG(note) FROM stage WHERE etat = "Terminé")
WHERE s.id_stage IS NULL;

WITH MoyenneNote AS (
    SELECT AVG(note) AS moyenne
    FROM stage
    WHERE etat = "Terminé"
)

SELECT nom_entreprise, adresse_entreprise
FROM entreprise
WHERE NOT EXISTS (
    SELECT 1
    FROM stage
    JOIN MoyenneNote ON stage.note < MoyenneNote.moyenne
    WHERE stage.id_entreprise = entreprise.id_entreprise
)