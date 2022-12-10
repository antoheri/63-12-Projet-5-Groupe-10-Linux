from tkinter import *
from gestionUtilisateursEtGroupes import *
from envoi_log import *

#Fonction création de la fenêtre basique
#va être appelée lors de chaque retour à l'interface principale
def basic_fen():
    #Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()
    #Création des différents Widgets / placer les éléments dans la fenêtre principale (fen_user)
    lab_acc: Label = Label(fen_user,text="Bonjour ! Que souhaitez-vous faire ?",font=("Courier",15,"bold"))
    butt_create_user= Button(fen_user, text="Créer un utilisateur",command=fen_create_user,borderwidth=5,width=25)
    butt_del_user = Button(fen_user, text="Supprimer un utilisateur",command=fen_del_user,borderwidth=5,width=25)
    butt_mod_user = Button(fen_user, text="Modifier un utilisateur",command=fen_modify_user,borderwidth=5,width=25)
    butt_create_group= Button(fen_user, text="Créer un groupe",command=fen_create_group,borderwidth=5,width=25)
    butt_del_group = Button(fen_user, text="Supprimer un groupe",command=fen_del_group,borderwidth=5,width=25)

    #Commande pour créer le Widget dans la fenêtre
    lab_acc.pack(pady=15)
    butt_create_user.pack(pady=15)
    butt_del_user.pack(pady=15)
    butt_mod_user.pack(pady=15)
    butt_create_group.pack(pady=15)
    butt_del_group.pack(pady=15)
#Fonction pour réinitialiser les composants de la fenêtre.
def fen_destruction():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fen_user.winfo_children():
        c.destroy()

#Fonction pour créer des label, elle prend en argument le texte et la postion dans la fenêtre par rapport à une grille
def create_label(text,row,column):

    text_entry= Label(fen_user, text=text, font=("bold", 15), justify='left')
    # Création des variables qui permetteront de récupérer les informations uitilisateurs
    input= StringVar()
    saisie= Entry(textvariable=input, width=30)

    # Formatage sous format de grille pour plus de clarté et pour aligner le label et la donnée que va rentrer l'utilisateur
    # .grid() correspond à .pack() utilisé dans d'autre méthodes mais avec des options différentes
    # paramètre sticky permet d'aligner le texte à gauche Format --> West,Est,South,NorthEst...
    text_entry.grid(row=row, column=column, pady=20, padx=30, sticky=W)

#Fonction pour créer des entrées utilisateurs, elle prend en argument la position dans la fenêtre
#password est un boolean, si true, le mot de passe est masqué lors de la saisie utilisateur
def create_entry(row,column,password):
    #Définition du type d'input que va recevoir l'entrée
    input= StringVar()

    #création du widget de saisie

    if(password==True):
        saisie = Entry(textvariable=input, width=30,show="*")
    else:
        saisie = Entry(textvariable=input, width=30)

    # Formatage sous format de grille pour plus de clarté et pour aligner le label et la donnée que va rentrer l'utilisateur
    # .grid() correspond à .pack() utilisé dans d'autre méthodes mais avec des options différentes
    # paramètre sticky permet d'aligner le texte à gauche Format --> West,Est,South,NorthEst...
    saisie.grid(row=row, column=column, pady=20)
    #returner la saisie pour utiliser les méthodes associées, c'est la *.get() qui nous intéresse pour récupérer
    # ce qui sera écrit pas l'utilisateur.
    return saisie


#Fonction pour la fenêtre de création d'un utilisateur
def fen_create_user():

    fen_destruction()

    create_label("Entrez le nom", 0, 0)
    entry_user_name = create_entry(0, 1,False)
    create_label("Entrez le mot de passe", 1, 0)
    entry_user_passwd= create_entry(1, 1,True)
    create_label("Entrez le mail", 2, 0)
    entry_mail = create_entry(2, 1,False)

    # Création des boutons pour appeler les futurs commandes de création
    # Obliger d'utiliser lambda pour passer des fonctions avec arguments
    # Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,
                        command=lambda: [add_user(entry_user_name.get(),entry_user_passwd.get()),
                        new_user(entry_user_name.get(),entry_mail.get()),
                        fen_create_user()])

    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)

    #Formatage des boutons
    butt_valid.grid(row=3, column=0,padx=20)
    butt_retour.grid(row=3, column=1,padx=20)

#Fonction pour la fenêtre de supression user
def fen_del_user():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()
    #Appel des fonctions pour créer les entrées.
    create_label("Indiquez le nom",0,0)
    entry_delete=create_entry(0,1,False)
    create_label("Indiquez un mail",1,0)
    entry_mail = create_entry(1,1,False)

    # Création du label de titre
    text_user = Label(fen_user,text="Utilisateurs",font=("Courier",15,"bold"))
    text_user.grid(row=2,columnspan=2)

    # Création de la liste où sera affichée les utilisateurs
    liste_groups = Listbox(fen_user, width=30, height=15)
    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(3,13):
        user = "user : "+ str(i)
        liste_groups.insert(i,user)
        liste_groups.grid(row=i,columnspan=2,padx=10)
    # Création des deux boutons
    # Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    butt_valid = Button(fen_user,text="Valider la supression",borderwidth=5,width=25,
                        command=lambda:[del_user(entry_delete.get()),
                        delete_user(entry_delete.get(),entry_mail.get()),
                        fen_del_user()])
    butt_retour = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)
    butt_valid.grid(row=14,column=0,pady=15,padx=10)
    butt_retour.grid(row=14,column=1,pady=15,padx=10)

#Fonction pour la fenêtre de modification d'utilisateur
def fen_modify_user():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()
    # Création du label de titre
    text_user = Label(fen_user,text="Que désirez-vous modifier ?",font=("Courier",15,"bold"))
    text_user.pack()

    butt_modify_name=Button(fen_user,text="Modifier le nom d'utilisateur",borderwidth=5, width=25,command=fen_modify_username)
    butt_modify_password = Button(fen_user,text="Modifier le mot de passe", borderwidth=5,width=25,command=fen_modify_password)
    butt_modify_group = Button(fen_user,text="Modifier le groupe de l'utilisateur", borderwidth=5,width=25,command=fen_modify_group)
    butt_retour_main = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)

    # Création des deux boutons, pour le retour arrière et pour la modification
    butt_modify_name.pack(pady=15)
    butt_modify_password.pack(pady=15)
    butt_modify_group.pack (pady=15)
    butt_retour_main.pack(pady=15)

#Fonction pour la fenêtre de modification du nom utilisateur
def fen_modify_username():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()
        # Création des Widgets de label

    create_label("Entrez l'ancien nom",0,0)
    entry_old_name = create_entry(0,1,False)
    create_label("Entrez le nouveau nom",1,0)
    entry_new_name = create_entry(1,1,False)
    create_label("Entrez le mail",2,0)
    entry_mail= create_entry(2,1,False)


    # Création des boutons pour appeler les futurs commandes de création
    # Obliger d'utiliser lambda pour passer des fonctions avec arguments
    # Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,
                        command=lambda: [modify_username(entry_old_name.get(),entry_new_name.get()),
                                         modify_user(entry_old_name.get(),entry_mail.get()),
                                         fen_modify_username()])

    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)

    # Formatage des boutons
    butt_valid.grid(row=3, column=0, padx=20)
    butt_retour.grid(row=3, column=1, padx=20)

#Fonction pour modifier le mot de passe
def fen_modify_password():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()
    # Création des Widgets de label

    create_label("Entrez l'utilisateur", 0, 0)
    entry_user_name = create_entry(0, 1,False)
    create_label("Entrez le mail", 1, 0)
    entry_mail = create_entry(1, 1,False)

    # Création des boutons pour appeler les futurs commandes de création
    # Obliger d'utiliser lambda pour passer des fonctions avec arguments
    # Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,
                        command=lambda: [modify_password(entry_user_name.get()),
                                         modify_user(entry_user_name.get(), entry_mail.get()),
                                         fen_modify_username()])


    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)

    # Formatage des boutons
    butt_valid.grid(row=3, column=0, padx=20)
    butt_retour.grid(row=3, column=1, padx=20)


    warning = Label(fen_user,text="Attention, Pour changer le mot de passe : ",font=("Courier",12,"bold"),bg="red")
    warning.grid(row=4,columnspan=2,pady=20)

    #Liste d'instruction pour l'utilisateur car on doit utiliser le shell pour réaliser une partie de l'opération
    instruction_list = Listbox(fen_user, width=60, height=15)
    instruction_list.insert(1,"1. Mettre le nom de l'utilisateur")
    instruction_list.grid(row=5,columnspan=2,pady=5)
    instruction_list.insert(2,"2. Mettre le mail")
    instruction_list.grid(row=6,columnspan=2,pady=5)
    instruction_list.insert(3,"3. Cliquer sur le bouton modifier")
    instruction_list.grid(row=7, columnspan=2, pady=5)
    instruction_list.insert(4,"4. Rentrer le mot de passe dans la ligne de commande du Shell")
    instruction_list.grid(row=8,columnspan=2,pady=5)

def fen_modify_group():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()

    # Création des Widgets de label et entrées
    create_label("Entrez l'utilisateur", 0, 0)
    entry_user_name = create_entry(0, 1,False)
    create_label("Entrez son nouveau groupe",1,0)
    entry_new_group=create_entry(1,1,False)
    create_label("Entrez le mail", 2, 0)
    entry_mail = create_entry(2, 1,False)

    # Création des boutons pour appeler les futurs commandes de création
    # Obliger d'utiliser lambda pour passer des fonctions avec arguments
    # Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,
                        command=lambda: [modify_users_group(entry_user_name.get(),entry_new_group.get()),
                                         modify_user(entry_user_name.get(),entry_mail.get()),
                                         fen_modify_group()])

    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)

    # Formatage des boutons
    butt_valid.grid(row=3, column=0, padx=20)
    butt_retour.grid(row=3, column=1, padx=20)


#Fenêtre de création groupe
def fen_create_group():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()

    # Création des Widgets de label et d'entrée
    create_label("Nom du groupe",0,0)
    entry_group_name=create_entry(0,1,False)
    create_label("Entrez un mail",1,0)
    entry_mail = create_entry(1,1,False)

    # Création des boutons pour appeler les futurs commandes de création
    # Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    # le bouton retour appel la méthode basic_fen qui revient à la fenêtre principale
    butt_valid = Button(fen_user, text="Valider la création / modification", borderwidth=5, width=25,
                        command=lambda:
                        [add_group(entry_group_name.get()),
                        new_group(entry_group_name.get(),entry_mail.get()),
                        fen_create_group()])
    butt_retour = Button(fen_user, text="Retour", borderwidth=5, width=25, command=basic_fen)


    #Formatage des boutons
    butt_valid.grid(row=3, column=0,padx=20)
    butt_retour.grid(row=3, column=1, padx=20)
#Fenêtre de supression groupe
def fen_del_group():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    fen_destruction()

    # Création des Widgets de label et d'entrée
    create_label("Nom du groupe", 0, 0)
    entry_group_name = create_entry(0, 1,False)
    create_label("Entrez un mail", 1, 0)
    entry_mail = create_entry(1, 1,False)
    # Création des deux boutons, pour le retour arrière et pour la suppression
    #Les boutons appellent les différentes fonctions pour l'action désirée / le mail / le FTP
    butt_valid = Button(fen_user,text="Valider la supression",borderwidth=5,width=25,
                        command=lambda:
                        [del_group(entry_group_name.get()),
                         delete_group(entry_group_name.get(),entry_mail.get()),
                         fen_del_group()])
    butt_retour = Button(fen_user,text="Retour",borderwidth=5,width=25,command=basic_fen)
    butt_valid.grid(row=3, column=0, padx=20)
    butt_retour.grid(row=3, column=1, padx=20)
#Fenêtre de modification de groupe

#Création de la fenêtre principale qui va nous servire pour l'entier de l'affichage
fen_user = Tk()
#Modification de la taille pour la rendre un peu plus grande
fen_user.geometry("600x600")
#Appel de la fonction basic_fen pour afficher la fenêtre d'accueil
basic_fen()


#Méthode pour dire à la fenêtre de rester affichée, sans cette appel elle n'apparaît pas
fen_user.mainloop()

