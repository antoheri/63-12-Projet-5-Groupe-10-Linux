
#Lister groupes et leurs utilisateurs
fileGroup = open("/etc/group")
print("Groupes".ljust(20)+"Utilisateurs du groupe")
lignes = fileGroup.readlines()
for ligne in lignes:

    print(ligne.split(':')[0].ljust(20)+ligne.split(':')[3])

fileGroup.close


#Lister utilisateurs
fileUsers = open("/etc/passwd")
print("Listes des utilisateurs :")
lignes = fileUsers.readlines()
for ligne in lignes:

    print(ligne.split(':')[0])
    print("")

fileUsers.close