import random
import faker

# Initialisation de Faker en français
fake = faker.Faker('fr_FR')

# Définition des domaines possibles
domaines = ['Informatique', 'Marketing', 'Finance', 'Ressources Humaines', 'Développement', 'Ventes', 'Support', 'Gestion', 'Direction', 'Production']

# Fonction pour générer un utilisateur fictif
def generer_utilisateur():
    nom = fake.last_name()
    prenom = fake.first_name()
    domaine = random.choice(domaines)
    espace_disque = f"{random.randint(50, 200)}GB"
    trafic = f"{random.randint(500, 3000)}GB"
    bande_passante = f"{random.randint(5, 20)}GB"
    admins = random.randint(1, 2)
    email = fake.email()
    password = fake.password(length=10)
    second_admin = fake.name() if random.choice([True, False]) else ""
    
    return (nom, prenom, domaine, espace_disque, trafic, bande_passante, admins, email, password, second_admin)
    
# Génération des utilisateurs
utilisateurs = [generer_utilisateur() for _ in range(600000)]

# Génération de la commande SQL
sql_commands = [
    "INSERT INTO utilisateurs (nom, prenom, domaine, espace_disque, trafic, bande_passante, admins, email, password, second_admin) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}');".format(
        utilisateur[0], utilisateur[1], utilisateur[2], utilisateur[3], utilisateur[4], utilisateur[5], utilisateur[6], utilisateur[7], utilisateur[8], utilisateur[9]
    ) for utilisateur in utilisateurs
]

# Affichage des 5 premières commandes SQL pour vérification
print('\n'.join(sql_commands[:60000]))
