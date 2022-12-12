import ftplib
from ftplib import FTP
import ssl

ftps = ftplib.FTP_TLS()


host = "d73kw.ftp.infomaniak.com" # adresse du serveur FTP
user = "d73kw_proj5_group10_lin" # identifiant
password = "4CnKx6M9Muw9" # mot de   passe
connect = FTP.ftplib(host,user,password) # on se connecte

connect.quit() # o� "connect" est le nom de la variable dans laquelle on a d�clar� la connexion 

fichier = "/6312_Python_2022/Proj5_Group10_Lin"
file = open(fichier, 'rb') # ici, j'ouvre le fichier ftp.py
connect.storbinary('STOR '+fichier, file) # ici (o� connect est encore la variable de la connexion), j'indique le fichier � envoyer
file.close() # on ferme le fichier

etat = connect.getwelcome() # gr�ce � la fonction getwelcome(), on r�cup�re le "message de bienvenue"
print ("Etat : ", etat) # ici, on l'affiche, cette ligne est facultative

rep = connect.dir() # on r�cup�re le listing
print (rep) # on l'affiche dans la console

commande = ('Tapez la commande � effectuer : ') # entrez la commande � effectuer
resultat = connect.sendcmd(commande) # on envoie la commande au serveur : si elle n'est pas bonne, Python plantera
