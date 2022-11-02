# 63-12-Projet-5-Groupe-10-Linux

Script python qui réalise un rapide audit de la situation actuelle des groupes et des utilisateurs sur un système linux.
Le script crée un fichier de log avec tous les utilisateurs/groupes actuels du système et envoi le fichier sur un serveur FTP.

Une interface utilisateur permet également à l’utilisateur d’ajouter, supprimer ou modifier un groupe ou un utilisateur. 
Lorsqu’un utilisateur est ajouté/modifié/supprimé, un mail d’information est envoyé à l'utilisateur du script.
Cette activité est loggée dans un second fichier où une nouvelle ligne est ajoutée contenant la date, l’heure, l’utilisateur ou le groupe (ajouté ou supprimé). 
Ce fichier est également envoyé sur le serveur FTP.
