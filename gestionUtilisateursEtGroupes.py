import os
import subprocess
import sys
import getpass
from datetime import datetime

# Fonction pour ajouter un utilisateur.
# Elle prend en paramètre le nom d'utilisateur (string) et le mot de passe (string) qui peut aussi être récupéré avec getpass pour plus de sécurité.
def add_user(username, password):
    home_directory = "/home/" + username

    try:
        subprocess.run(['sudo', 'useradd', '-s', '/bin/bash', '-m', '-d', home_directory, username, '-p', password])
    except:
        print(f"L'ajout de l'utilisaeur {username} n'a pas fonctionné")
        sys.exit(1)


# Fonction pour supprimer un utilisateur, elle prend en argument le nom de l'tuilisateur (string).
def del_user(username):
    try:
        subprocess.run(['sudo', 'userdel', '-r', username])
    except:
        print(f"La suppression de l'utilisaeur {username} n'a pas fonctionné")

# Fonction pour ajouter un groupe, elle prend en argument le nom du groupe (string).
def add_group(groupname):
    try:
        subprocess.run(['sudo', 'groupadd', groupname])
    except:
        print(f"L'ajout du groupe {groupname} n'a pas fonctionné")

# Fonction pour supprimer un groupe, elle prend en argument le nom du groupe (string).
def del_group(groupname):
    try:
        subprocess.run(['sudo', 'groupdel', groupname])
    except:
        print(f"L'ajout du groupe {groupname} n'a pas fonctionné")

# Fonction pour ajouter un utilisateur à un groupe, elle prend en argument le nom d'utilisateur (string) et
# le nom du nouveau groupe (string) qui remplacera celui d'avant. Attention, ce groupe doit déjà être existant
def modify_users_group(user, new_group):
    try:
        subprocess.run(['sudo', 'usermod', '-aG', new_group, user])
    except:
        print(f"La modifiaction du groupe n'a pas fonctionné")
        
# Fonction pour modifier le nom d'un utilisateur, elle prend en argument l'ancien et le nouveau nom d'utilisateur (string).
def modify_username(user, new_username):
    try:
        subprocess.run(['sudo', 'usermod', '-l', new_username, user])
    except:
        print(f"La modifiaction du nom d'utilisateur n'a pas fonctionné")
        
# Fonction pour ajouter un groupe, elle prend en argument le nom d'utilisateur (string).
# Le mot de passe est entré de manière interactive avec le shell.
def modify_password(user):
    try:
        subprocess.run(['sudo', 'passwd', user])
    except:
        print(f"La modification du nom d'utilisateur n'a pas fonctionné.")
# Fonction pour la gestion d'un fichier de logs, celui-ci est créé dans le dossier courant.
def modify_log_file(text_to_append):
    current_datetime = datetime.now()
    formated_datetime = current_datetime.strftime("%d/%m/%Y, %H:%M:%S")
    with open("modifications.log", "a") as file:
        file.write("[" + formated_datetime + "] " + text_to_append)
        file.write("\n")
