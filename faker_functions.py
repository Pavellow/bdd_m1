from faker import Faker

# Création d'instances Faker pour le français et l'italien
faker = Faker('fr_FR')

# Fonction pour générer une personne avec un nom français et un nom italien
def generate_person():
    return faker.name()

print(generate_person())