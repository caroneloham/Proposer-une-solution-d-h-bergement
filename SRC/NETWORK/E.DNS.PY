import os
import tkinter as tk
from tkinter import messagebox

# Chemins des fichiers de configuration mis à jour
nginx_conf_path = 'C:/Users/Administrateur/Desktop/nginx-1.25.4/conf/nginx.conf'
sites_available_path = 'C:/Users/Administrateur/Desktop/nginx-1.25.4/conf/sites-available/'
hosts_file_path = 'C:/Windows/System32/drivers/etc/hosts'

def create_site_conf(domain_name, site_directory):
    conf_text = f"""server {{
    listen 80;
    server_name {domain_name};

    location / {{
        root html/{site_directory};
        index index.html index.htm;
    }}
}}
"""
    conf_file_path = os.path.join(sites_available_path, f'{domain_name}.conf')
    with open(conf_file_path, 'w') as file:
        file.write(conf_text)
    return conf_file_path

def update_nginx_conf(new_site_conf):
    with open(nginx_conf_path, 'r+') as file:
        lines = file.readlines()
        insert_line = None
        for i, line in enumerate(lines):
            if "include sites-available/" in line:
                insert_line = i + 1 # Ajoute une ligne après la dernière entrée include

        if insert_line:
            lines.insert(insert_line, f'    include {new_site_conf};\n')
            file.seek(0)
            file.writelines(lines)

def update_hosts_file(domain_name):
    with open(hosts_file_path, 'a') as file:
        file.write(f'127.0.0.1 {domain_name}\n')

def automate_dns(domain_name, site_directory):
    # Crée le fichier de configuration du site
    new_site_conf = create_site_conf(domain_name, site_directory)
    # Met à jour nginx.conf pour inclure la configuration du nouveau site
    update_nginx_conf(os.path.join('sites-available', f'{domain_name}.conf'))
    # Met à jour le fichier hosts de Windows
    update_hosts_file(domain_name)

# Interface graphique
root = tk.Tk()
root.title('Configuration DNS et Serveur Web')

# Étiquettes
domain_label = tk.Label(root, text="Nom de domaine:")
domain_label.grid(row=0, column=0, sticky="e")

directory_label = tk.Label(root, text="Répertoire du site:")
directory_label.grid(row=1, column=0, sticky="e")

# Champs de saisie
domain_entry = tk.Entry(root)
domain_entry.grid(row=0, column=1)

directory_entry = tk.Entry(root)
directory_entry.grid(row=1, column=1)

# Fonction pour le bouton
def submit():
    domain_name = domain_entry.get()
    site_directory = directory_entry.get()
    if domain_name and site_directory:
        try:
            automate_dns(domain_name, site_directory)
            messagebox.showinfo('Succès', 'La configuration a été ajoutée avec succès.')
        except Exception as e:
            messagebox.showerror('Erreur', f'Une erreur est survenue: {e}')
    else:
        messagebox.showwarning('Avertissement', 'Veuillez entrer le nom de domaine et le répertoire du site.')

# Bouton de soumission
submit_button = tk.Button(root, text="Configurer", command=submit)
submit_button.grid(row=2, column=0, columnspan=2)

# Exécution de l'interface graphique
root.mainloop()
