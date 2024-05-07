import mysql.connector
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Configuration de la connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="Eloham",
    password="Webap1942",
    database="infra_mngt"  # Remplacez par le nom de votre base de données
)
cursor = conn.cursor()

HTML_FORM = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cybersécurité et Réseaux</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>OVH</h1>
    </header>
    <main>
        <section id="formulaire-inscription">
            <h2>Inscription</h2>
            <form action="/" method="post">
                <!-- Vos champs de formulaire ici -->
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 GROUPE SISR</p>
    </footer>
</body>
<style>
    <!-- Votre CSS ici -->
</style>
</html>'''

@app.route("/", methods=["GET", "POST"])
def formulaire():
    if request.method == "POST":
        # Récupérer les données du formulaire
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        domaine = request.form.get("domaine")
        espace_disque = request.form.get("espace-disque")
        trafic = request.form.get("trafic")
        bande_passante = request.form.get("bande-passante")
        admins = request.form.get("admins")
        email = request.form.get("email")
        password = request.form.get("password")
        second_admin = request.form.get("second-admin")

        # Insérer les données dans la base de données
        sql = "INSERT INTO utilisateurs (nom, prenom, domaine, espace_disque, trafic, bande_passante, admins, email, password, second_admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, domaine, espace_disque, trafic, bande_passante, admins, email, password, second_admin)
        cursor.execute(sql, values)
        conn.commit()

        return "Formulaire soumis avec succès !"
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)
