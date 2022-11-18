import os
import subprocess
import sys
import getpass

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
