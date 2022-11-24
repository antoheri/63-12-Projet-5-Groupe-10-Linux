from tkinter import *
import os
import subprocess
import sys
from gestionUtilisateursEtGroupes import *
from functools import partial
import getpass

# Fonction pour ajouter un utilisateur.
# Elle prend en paramètre le nom d'utilisateur (string) et le mot de passe (string) qui peut aussi être récupéré avec getpass pour plus de sécurité.
#Fonction création de la fenêtre basique
#va être appelée lors de chaque retour à l'interface principale
def basic_fen():
    #Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()
    #Création des différents Widgets / placer les éléments dans la fenêtre principale (fen_user)
    lab_acc: Label = Label(fen_user,text="Bonjour ! Que souhaitez-vous faire ?",font=("Courier",15,"bold"))
    butt_create_user= Button(fen_user, text="Créer un utilisateur",command=fen_create_user,borderwidth=5,width=25)
    butt_del_user = Button(fen_user, text="Supprimer un utilisateur",command=fen_del_user,borderwidth=5,width=25)
    butt_mod_user = Button(fen_user, text="Modifier un utilisateur",command=fen_modify_user,borderwidth=5,width=25)
    butt_create_group= Button(fen_user, text="Créer un groupe",command=fen_create_group,borderwidth=5,width=25)
    butt_del_group = Button(fen_user, text="Supprimer un groupe",command=fen_del_group,borderwidth=5,width=25)
    butt_mod_group = Button(fen_user, text="Modifier un groupe",command=fen_modify_group,borderwidth=5,width=25)

    #Commande pour créer le Widget dans la fenêtre
    lab_acc.pack(pady=15)
    butt_create_user.pack(pady=15)
    butt_del_user.pack(pady=15)
    butt_mod_user.pack(pady=15)
    butt_create_group.pack(pady=15)
    butt_del_group.pack(pady=15)
    butt_mod_group.pack(pady=15)
#Fenêtre de création d'un utilisateur
def fen_create_user():
    #Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()
    # Création des Widgets de label
    text_entry_user = Label(fen_user, text='Entrer Identifiant:', font=("bold", 15), justify='left')
    text_entry_pass = Label(fen_user, text='Entrer le password :', font=("bold", 15), justify='left')
    text_entry_mail = Label(fen_user, text='Entrer votre mail :', font=("bold", 15), justify='left')

    #Création des variables qui permetteront de récupérer les informations uitilisateurs
    input_user_name = StringVar()
    input_user_pass = StringVar()
    input_user_mail = StringVar()
    saisie_pass = Entry(textvariable=input_user_pass, width=30)
    saisie_user = Entry(textvariable=input_user_name,width=30)
    saisie_mail = Entry(textvariable=input_user_mail, width=30)

    # Création des boutons pour appeler les futurs commandes de création
    # Obliger d'utiliser lambda pour passer des fonctions avec arguments
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,
                        command=lambda: add_user(saisie_user.get(), saisie_pass.get()))
    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)

    #Formatage sous format de grille pour plus de clarté et pour aligner le label et la donnée que va rentrer l'utilisateur
    #.grid() correspond à .pack() utilisé dans d'autre méthodes mais avec des options différentes
    # paramètre sticky permet d'aligner le texte à gauche Format --> West,Est,South,NorthEst...
    text_entry_user.grid(row=0, column=0,pady=20,padx=30,sticky=W)
    text_entry_pass.grid(row=1,column=0,pady=40,padx=30,sticky=W)
    text_entry_mail.grid(row=2, column=0, pady=40,padx=30,sticky=W)

    #Formatage des cases où écrira l'utilisateur.
    saisie_user.grid(row=0, column=1, pady=20)
    saisie_pass.grid(row=1, column=1, pady=40)
    saisie_mail.grid(row=2, column=1, pady=40)

    #Formatage des boutons
    butt_valid.grid(row=4, column=0,padx=20)
    butt_retour.grid(row=4, column=1,padx=20)

#Fenêtre de supression user
def fen_del_user():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()
    #Création du label de titre
    text_user = Label(fen_user,text="Voici la liste de vos utilisateurs",font=("Courier",15,"bold"))

    #Création de la liste où sera affichée les utilisateurs
    liste_groups = Listbox(fen_user, width=60, height=20)

    #Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "Utilisateur numéro : "+ str(i)
        liste_groups.insert(i,user)
    liste_groups.pack()

    #Création du label pour l'utilisateur et de l'entrée pour son mail
    text_entry_mail = Label(fen_user, text='Entrez votre mail :', font=("bold", 15), justify='left')
    input_user_mail = StringVar()
    saisie_mail = Entry(textvariable=input_user_mail, width=30)

    #Création du label pour recevoir le nom de l'utilisateur à supprimer
    text_entry_user = Label(fen_user, text="Entrez le nom de l'utilisateur", font=("bold", 15), justify='left')
    input_user_name = StringVar()
    saisie_user = Entry(textvariable=input_user_name, width=30)

    #Création des deux boutons, pour le retour arrière et pour la suppression
    #utilisation de lambda pour faire fonctionner une fonction avec argument
    butt_valid = Button(fen_user,text="Valider la supression",borderwidth=5,width=25,command=lambda:del_user(saisie_user.get()))
    butt_retour = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)

    #Formatage des boutons
    butt_valid.pack(side=LEFT,padx=25)
    butt_retour.pack(side=RIGHT,padx=25)
    #Formatage des entrée utilisateurs et des labels
    text_user.pack()
    text_entry_user.pack(padx=25, pady=10)
    saisie_user.pack(padx=25)
    text_entry_mail.pack(padx=25,pady=10)
    saisie_mail.pack(padx=25)

#Fenêtre de modification user
def fen_modify_user():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()
    # Création du label de titre
    text_user = Label(fen_user,text="Voici la liste de vos utilisateurs",font=("Courier",15,"bold"))
    text_user.pack()

    # Création de la liste où sera affichée les utilisateurs
    liste_groups = Listbox(fen_user, width=60, height=25)

    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "Utilisateur numéro : "+ str(i)
        liste_groups.insert(i,user)
    liste_groups.pack()
    # Création des deux boutons, pour le retour arrière et pour la modification
    butt_valid = Button(fen_user,text="Modifier l'utilisateur",borderwidth=5,width=25,command=fen_create_user)
    butt_retour = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)
    butt_valid.pack(side=LEFT,padx=25)
    butt_retour.pack(side=RIGHT,padx=25)
#Fenêtre de création groupe
def fen_create_group():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()

    # Création des Widgets de label
    text_entry_group = Label(fen_user, text='Entrez nom du groupe:', font=("bold", 15), justify='left')
    text_entry_mail = Label(fen_user, text='Entrez votre mail :', font=("bold", 15), justify='left')

    # Création des variables qui permetteront de récupérer les informations uitilisateurs
    input_group_name = StringVar()
    input_user_mail = StringVar()
    saisie_group = Entry(textvariable=input_group_name, width=30)
    saisie_mail = Entry(textvariable=input_user_mail, width=30)

    # Création des boutons pour appeler les futurs commandes de création
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,command=lambda:add_group(saisie_group.get()))
    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)

    # Formatage sous format de grille pour plus de clarté et pour aligner le label et la donnée que va rentrer l'utilisateur
    # .grid() correspond à .pack() utilisé dans d'autre méthodes mais avec des options différentes
    # paramètre sticky permet d'aligner le texte à gauche Format --> West,Est,South,NorthEst...
    text_entry_group.grid(row=0, column=0, pady=20, padx=30, sticky=W)
    text_entry_mail.grid(row=1, column=0, pady=40, padx=30, sticky=W)

    #Formatage des boutons
    butt_valid.grid(row=3, column=0,padx=20)
    butt_retour.grid(row=3, column=1, padx=20)

    # Formatage des cases où écrira l'utilisateur.
    saisie_group.grid(row=0, column=1, pady=20)
    saisie_mail.grid(row=1, column=1, pady=40)
#Fenêtre de supression groupe
def fen_del_group():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()
    # Création du label de titre
    text_user = Label(fen_user,text="Voici la liste de vos groupe",font=("Courier",15,"bold"))
    text_user.pack()

    # Création de la liste où sera affichée les utilisateurs
    liste_groups = Listbox(fen_user, width=60, height=20)

    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "groupe numéro : "+ str(i) + " --utilisateur xy"
        liste_groups.insert(i,user)
    liste_groups.pack()

    # Création du label et de l'entrée pour le mail de l'utilisateur
    text_user_mail = Label(fen_user, text='Entrez votre mail :', font=("bold", 15), justify='left')
    input_user_mail = StringVar()
    saisie_mail = Entry(textvariable=input_user_mail, width=30)
    text_user_mail.pack(padx=25,pady=10)
    saisie_mail.pack(padx=25)

    # Création du label et de l'entrée pour le groupe
    text_entry_group = Label(fen_user, text='Entrez le groupe', font=("bold", 15), justify='left')
    input_group = StringVar()
    saisie_group = Entry(textvariable=input_group, width=30)
    text_entry_group.pack(padx=25, pady=10)
    saisie_group.pack(padx=25)

    # Création des deux boutons, pour le retour arrière et pour la suppression
    butt_valid = Button(fen_user,text="Valider la supression",borderwidth=5,width=25,command=lambda:del_group(saisie_group.get()))
    butt_retour = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)
    butt_valid.pack(side=LEFT,padx=25)
    butt_retour.pack(side=RIGHT,padx=25)
#Fenêtre de modification de groupe
def fen_modify_group():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()
    # Création du label de titre
    text_user = Label(fen_user,text="Voici la liste de vos groupes",font=("Courier",15,"bold"))
    text_user.pack()

    # Création de la liste où sera affichée les utilisateurs
    liste_groups = Listbox(fen_user, width=60, height=25)

    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "groupe numéro : "+ str(i) +" --utilisateur xy"
        liste_groups.insert(i,user)
    liste_groups.pack()
    # Création des deux boutons, pour le retour arrière et pour la suppression
    butt_valid = Button(fen_user,text="Modifier le groupe",borderwidth=5,width=25,command=fen_create_user)
    butt_retour = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)
    butt_valid.pack(side=LEFT,padx=25)
    butt_retour.pack(side=RIGHT,padx=25)

#Création de la fenêtre principale qui va nous servire pour l'entier de l'affichage
fen_user = Tk()
#Modification de la taille pour la rendre un peu plus grande
fen_user.geometry("600x600")
#Appel de la fonction basic_fen pour afficher la fenêtre d'accueil
basic_fen()


#Méthode pour dire à la fenêtre de rester affichée, sans cette appel elle n'apparaît pas
fen_user.mainloop()