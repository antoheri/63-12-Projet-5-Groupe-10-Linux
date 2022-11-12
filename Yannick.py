from tkinter import *

#Fonction création de la fenêtre basique
#va être appelée lors de chaque retour à l'interface principale
def basicFen():
    #Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    #Création des différents Widgets / placer les éléments dans la fenêtre principale (fenUser)
    labAcc = Label(fenUser,text="Bonjour ! Que souhaitez-vous faire ?",font=("Courier",15,"bold"))
    buttCreateUser= Button(fenUser, text="Créer un utilisateur",command=createUser,borderwidth=5,width=25)
    buttDelUser = Button(fenUser, text="Supprimer un utilisateur",command=delUser,borderwidth=5,width=25)
    buttModUser = Button(fenUser, text="Modifier un utilisateur",command=modifyUser,borderwidth=5,width=25)
    buttCreateGroup= Button(fenUser, text="Créer un groupe",command=createGroup,borderwidth=5,width=25)
    buttDelGroup = Button(fenUser, text="Supprimer un groupe",command=delGroup,borderwidth=5,width=25)
    buttModGroup = Button(fenUser, text="Modifier un groupe",command=modifyGroup,borderwidth=5,width=25)

    #Commande pour créer le Widget dans la fenêtre
    labAcc.pack(pady=15)
    buttCreateUser.pack(pady=15)
    buttDelUser.pack(pady=15)
    buttModUser.pack(pady=15)
    buttCreateGroup.pack(pady=15)
    buttDelGroup.pack(pady=15)
    buttModGroup.pack(pady=15)
#Fenêtre de création d'un utilisateur
def createUser():
    #Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    #Création des Widgets de label
    textEntryUser = Label(fenUser, text='Entrer le login :',font=("bold",15),justify='left')
    textEntryPass = Label(fenUser, text='Entrer le password :',font=("bold",15),justify='left')
    textEntryName = Label(fenUser, text='Entrer le nom complet :',font=("bold",15),justify='left')
    textEntryMail = Label(fenUser, text='Entrer votre mail :',font=("bold",15),justify='left')

    #Création des différentes entrées qui serviront à récolter les infos de l'utilisateur
    #EntryPass donne le format de l'entrée
    #saisie servira pour la méthode get pour récupérer le contenu et l'utiliser dans les méthodes de création
    entryPass = StringVar()
    entryUser = StringVar()
    entryName = StringVar()
    entryMail = StringVar()
    saisieUser = Entry(textvariable=entryUser,width=30)
    saisiePass = Entry(textvariable=entryPass,width=30)
    saisieUserName = Entry(textvariable=entryName,width=30)
    saisieMail = Entry(textvariable=entryMail,width=30)

    #Création des boutons pour appeler les futurs commandes de création
    #le bouton retour appel la méthode basicFen qui revient à la fenêtre principale
    buttValid = Button(fenUser,text="Valider la création / modification",borderwidth=5,width=25)
    buttRetour = Button(fenUser,text="Retour",borderwidth=5,width=25,command=basicFen)

    #Formatage sous format de grille pour plus de clarté et pour aligner l'entrée et la définition
    #.grid() correspond à .pack() utilisé dans d'autre méthodes mais avec des options différentes
    # paramètre sticky permet d'aligner le texte à gauche Format --> West,Est,South,NorthEst...
    textEntryUser.grid(row=0, column=0,pady=20,padx=30,sticky=W)
    saisieUser.grid(row=0,column=1,pady=20)
    textEntryPass.grid(row=1,column=0,pady=40,padx=30,sticky=W)
    saisiePass.grid(row=1,column=1,pady=40)
    textEntryName.grid(row=2,column=0,pady=40,padx=30,sticky=W)
    saisieUserName.grid(row=2,column=1,pady=40)
    textEntryMail.grid(row=3, column=0, pady=40,padx=30,sticky=W)
    saisieMail.grid(row=3, column=1, pady=40)
    buttValid.grid(row=4,column=0)
    buttRetour.grid(row=4,column=1,)
#Fenêtre de supression user
def delUser():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    #Création du label de titre
    textUser = Label(fenUser,text="Voici la liste de vos utilisateurs",font=("Courier",15,"bold"))
    textUser.pack()

    #Création de la liste où sera affichée les utilisateurs
    listeGroups = Listbox(fenUser, width=60, height=20)

    #Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "Utilisateur numéro : "+ str(i)
        listeGroups.insert(i,user)
    listeGroups.pack()

    #Création du label et de l'entrée pour le mail de l'utilisateur
    textEntryMail = Label(fenUser, text='Entrer votre mail :', font=("bold", 15), justify='left')
    entryMail = StringVar()
    saisieMail = Entry(textvariable=entryMail, width=30)
    textEntryMail.pack(padx=25,pady=10)
    saisieMail.pack(padx=25)

    #Création des deux boutons, pour le retour arrière et pour la suppression
    buttValid = Button(fenUser,text="Valider la supression",borderwidth=5,width=25)
    buttRetour = Button(fenUser,text="Retour",borderwidth=5,width=25,command=basicFen)
    buttValid.pack(side=LEFT,padx=25)
    buttRetour.pack(side=RIGHT,padx=25)
#Fenêtre de modification user
def modifyUser():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    # Création du label de titre
    textUser = Label(fenUser,text="Voici la liste de vos utilisateurs",font=("Courier",15,"bold"))
    textUser.pack()

    # Création de la liste où sera affichée les utilisateurs
    listeGroups = Listbox(fenUser, width=60, height=25)

    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "Utilisateur numéro : "+ str(i)
        listeGroups.insert(i,user)
    listeGroups.pack()
    # Création des deux boutons, pour le retour arrière et pour la modification
    buttValid = Button(fenUser,text="Modifier l'utilisateur",borderwidth=5,width=25,command=createUser)
    buttRetour = Button(fenUser,text="Retour",borderwidth=5,width=25,command=basicFen)
    buttValid.pack(side=LEFT,padx=25)
    buttRetour.pack(side=RIGHT,padx=25)
#Fenêtre de création groupe
def createGroup():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    # Création des Widgets de label
    textEntryUser = Label(fenUser, text='Entrer le nom du groupe:', font=("bold", 15), justify='left')
    textEntryPass = Label(fenUser, text='Info X:', font=("bold", 15), justify='left')
    textEntryName = Label(fenUser, text='Entrer le nom complet :', font=("bold", 15), justify='left')
    textEntryMail = Label(fenUser, text='Entrer votre mail :', font=("bold", 15), justify='left')

    # Création des différentes entrées qui serviront à récolter les infos de l'utilisateur
    # EntryPass donne le format de l'entrée
    # saisie servira pour la méthode get pour récupérer le contenu et l'utiliser dans les méthodes de création
    entryPass = StringVar()
    entryUser = StringVar()
    entryName = StringVar()
    entryMail = StringVar()
    saisieUser = Entry(textvariable=entryUser, width=30)
    saisiePass = Entry(textvariable=entryPass, width=30)
    saisieUserName = Entry(textvariable=entryName, width=30)
    saisieMail = Entry(textvariable=entryMail, width=30)

    # Création des boutons pour appeler les futurs commandes de création
    # le bouton retour appel la méthode basicFen qui revient à la fenêtre principale
    buttValid = Button(fenUser, text="Valider la création / modification", borderwidth=5, width=25)
    buttRetour = Button(fenUser, text="Retour", borderwidth=5, width=25, command=basicFen)

    # Formatage sous format de grille pour plus de clarté et pour aligner l'entrée et la définition
    # .grid() correspond à .pack() utilisé dans d'autre méthodes mais avec des options différentes
    # paramètre sticky permet d'aligner le texte à gauche Format --> West,Est,South,NorthEst...
    textEntryUser.grid(row=0, column=0, pady=20, padx=30, sticky=W)
    saisieUser.grid(row=0, column=1, pady=20)
    textEntryPass.grid(row=1, column=0, pady=40, padx=30, sticky=W)
    saisiePass.grid(row=1, column=1, pady=40)
    textEntryName.grid(row=2, column=0, pady=40, padx=30, sticky=W)
    saisieUserName.grid(row=2, column=1, pady=40)
    textEntryMail.grid(row=3, column=0, pady=40, padx=30, sticky=W)
    saisieMail.grid(row=3, column=1, pady=40)
    buttValid.grid(row=4, column=0)
    buttRetour.grid(row=4, column=1, )
#Fenêtre de supression groupe
def delGroup():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    # Création du label de titre
    textUser = Label(fenUser,text="Voici la liste de vos groupe",font=("Courier",15,"bold"))
    textUser.pack()

    # Création de la liste où sera affichée les utilisateurs
    listeGroups = Listbox(fenUser, width=60, height=20)

    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "groupe numéro : "+ str(i) + " --utilisateur xy"
        listeGroups.insert(i,user)
    listeGroups.pack()

    # Création du label et de l'entrée pour le mail de l'utilisateur
    textEntryMail = Label(fenUser, text='Entrer votre mail :', font=("bold", 15), justify='left')
    entryMail = StringVar()
    saisieMail = Entry(textvariable=entryMail, width=30)
    textEntryMail.pack(padx=25,pady=10)
    saisieMail.pack(padx=25)

    # Création des deux boutons, pour le retour arrière et pour la suppression
    buttValid = Button(fenUser,text="Valider la supression",borderwidth=5,width=25)
    buttRetour = Button(fenUser,text="Retour",borderwidth=5,width=25,command=basicFen)
    buttValid.pack(side=LEFT,padx=25)
    buttRetour.pack(side=RIGHT,padx=25)
#Fenêtre de modification de groupe
def modifyGroup():
    # Supprime l'ancien contenu pour afficher le nouveau à chaque appel
    for c in fenUser.winfo_children():
        c.destroy()
    # Création du label de titre
    textUser = Label(fenUser,text="Voici la liste de vos groupes",font=("Courier",15,"bold"))
    textUser.pack()

    # Création de la liste où sera affichée les utilisateurs
    listeGroups = Listbox(fenUser, width=60, height=25)

    # Juste une boucle de test pour montrer comment utiliser la liste, il faut insérer les éléments avec un index
    for i in range(0,10):
        user = "groupe numéro : "+ str(i) +" --utilisateur xy"
        listeGroups.insert(i,user)
    listeGroups.pack()
    # Création des deux boutons, pour le retour arrière et pour la suppression
    buttValid = Button(fenUser,text="Modifier le groupe",borderwidth=5,width=25,command=createUser)
    buttRetour = Button(fenUser,text="Retour",borderwidth=5,width=25,command=basicFen)
    buttValid.pack(side=LEFT,padx=25)
    buttRetour.pack(side=RIGHT,padx=25)

#Création de la fenêtre principale qui va nous servire pour l'entier de l'affichage
fenUser = Tk()
#Modification de la taille pour la rendre un peu plus grande
fenUser.geometry("600x600")
#Appel de la fonction basicFen pour afficher la fenêtre d'accueil
basicFen()
#Méthode pour dire à la fenêtre de rester affichée, sans cette appel elle n'apparaît pas
fenUser.mainloop()