import tkinter as tk
from tkinter import ttk

# Fonction pour soumettre les données
def soumettre():
    # Ici, vous pouvez ajouter le code pour utiliser ou stocker les informations saisies
    print("Informations soumises :")
    print(f"Nom : {entry_nom.get()}")
    print(f"Prénom : {entry_prenom.get()}")
    print(f"Nom de domaine : {entry_domaine.get()}")
    print(f"Besoin en espace disque : {entry_espace_disque.get()}")
    print(f"Trafic attendu : {entry_trafic.get()}")
    print(f"Besoins en bande passante : {entry_bande_passante.get()}")
    print(f"Nombre d’administrateurs : {entry_nb_admin.get()}")
    print(f"Adresse email : {entry_email.get()}")
    print(f"Mot de passe : {entry_mdp.get()}")
    print(f"Deuxième administrateur : {entry_admin2.get()}")
    
    # Effacer les champs après soumission
    for entry in entries:
        entry.delete(0, tk.END)
        
# Initialisation de la fenêtres
fenetre = tk.Tk()
fenetre.title("Formulaire d'inscription")

# Création des champs de formulaire
labels = ["Nom", "Prénom", "Nom de domaine", "Besoin en espace disque", "Trafic attendu", "Besoins en bande passante",
          "Nombre d’administrateurs", "Adresse email", "Mot de passe", "Deuxième administrateur"]
entries = []

for i, label in enumerate(labels):
    ttk.Label(fenetre, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry_var = tk.Entry(fenetre)
    entry_var.grid(row=i, column=1, padx=10, pady=5, sticky="e")
    entries.append(entry_var)

entry_nom, entry_prenom, entry_domaine, entry_espace_disque, entry_trafic, entry_bande_passante, entry_nb_admin, entry_email, entry_mdp, entry_admin2 = entries

# Boutons pour soumettre ou effacer les informations
ttk.Button(fenetre, text="Soumettre", command=soumettre).grid(row=len(labels), column=0, padx=10, pady=10, sticky="w")
ttk.Button(fenetre, text="Effacer", command=lambda: [entry.delete(0, tk.END) for entry in entries]).grid(row=len(labels), column=1, padx=10, pady=10, sticky="e")

# Démarrage de l'interface graphique
fenetre.mainloop()
