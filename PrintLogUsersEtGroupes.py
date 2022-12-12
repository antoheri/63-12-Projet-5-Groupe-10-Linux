def list_group():
    # Lister les groupes et leurs utilisateurs
    fileGroup = open("/etc/group")

    chaine="\n"+"Groupes".ljust(20) + "Utilisateurs du groupe "+"\n"
    lignes = fileGroup.readlines()
    for ligne in lignes:
        chaine+=(ligne.split(':')[0].ljust(20) + ligne.split(':')[3]+"\n")

    fileGroup.close
    return chaine

def list_modify_group(group):
    message = "Le groupe "+group+" a été modifié"
    return message

def list_modify_user(user):
    message = "L'utilisateur "+user+" a été modifié"
    return message

def list_users():
    # Lister tous les utilisateurs
    fileUsers = open("/etc/passwd")
    chaine="\n""Liste de tous les utilisateurs :" + "\n"
    lignes = fileUsers.readlines()
    for ligne in lignes:
        chaine+=(ligne.split(':')[0]+ "\n")

    fileUsers.close
    return chaine


