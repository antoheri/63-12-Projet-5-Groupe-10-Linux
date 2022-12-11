
#Lister groupes et leurs utilisateurs
fileGroup = open("/etc/group")
print("Groupes".ljust(20)+"Utilisateurs du groupe")
print("")
lignes = fileGroup.readlines()
for ligne in lignes:

    print(ligne.split(':')[0].ljust(20)+ligne.split(':')[3])

fileGroup.close


#Lister tous les utilisateurs 
fileUsers = open("/etc/passwd")
print("Liste de tous les utilisateurs :")
print("")
lignes = fileUsers.readlines()
for ligne in lignes:

    print(ligne.split(':')[0])
    print("")

fileUsers.close
