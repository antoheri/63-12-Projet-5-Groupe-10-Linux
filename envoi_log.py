import smtplib


#username = nom d'utilisateur et le mail est le mail de celui qui modifie les utilisateurs ou les groupes
def new_user(username, mail):

    # Configuration SMTP
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = "envoielogpyhton@gmail.com" # email Gmail
    mdp_smtp = "lsertysnmuzindln"  # mot de passe

    # Texte de l'email
    prenom = username
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour {prenom}, le nouveau utilisateur {prenom} a été créé. {formule_p}'

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp) # cette configuration fonctionne pour gmail
    mail.ehlo() # protocole pour SMTP étendu
    mail.starttls() # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()

def delete_user(username, mail):

    # Configuration SMTP
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = "envoielogpyhton@gmail.com" # email Gmail
    mdp_smtp = "lsertysnmuzindln"  # mot de passe

    # Texte de l'email
    prenom = username
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f"Bonjour {prenom}, l'utilisateur {prenom} a été supprimé. {formule_p}"

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp) # cette configuration fonctionne pour gmail
    mail.ehlo() # protocole pour SMTP étendu
    mail.starttls() # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()

def modify_user(username, mail):

    # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = "envoielogpyhton@gmail.com" # Mon email Gmail
    mdp_smtp = "lsertysnmuzindln"  # Mon mot de passe

    # Texte de l'email
    prenom = username
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f"Bonjour {prenom}, l'utilisateur {prenom} a été modifié. {formule_p}"

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp) # cette configuration fonctionne pour gmail
    mail.ehlo() # protocole pour SMTP étendu
    mail.starttls() # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()

def new_group(groupname, mail):

    # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = "envoielogpyhton@gmail.com"  # Mon email Gmail
    mdp_smtp = "lsertysnmuzindln"  # Mon mot de passe

    #Texte de l'email
    
    group = groupname
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour, le nouveau groupe {group} a été créé. {formule_p}'

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp)  # cette configuration fonctionne pour gmail
    mail.ehlo()  # protocole pour SMTP étendu
    mail.starttls()  # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()

def delete_group(groupname, mail):

    # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = "envoielogpyhton@gmail.com"  # Mon email Gmail
    mdp_smtp = "lsertysnmuzindln"  # Mon mot de passe

    # Texte de l'email
    
    group = groupname
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour, le groupe {group} a été supprimé. {formule_p}'

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp)  # cette configuration fonctionne pour gmail
    mail.ehlo()  # protocole pour SMTP étendu
    mail.starttls()  # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()

def modify_group(groupname, mail):

    # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = "envoielogpyhton@gmail.com"  # Mon email Gmail
    mdp_smtp = "lsertysnmuzindln"  # Mon mot de passe

    # Texte de l'email
 
    group = groupname
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour, le groupe {group} a été modifié. {formule_p}'

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp)  # cette configuration fonctionne pour gmail
    mail.ehlo()  # protocole pour SMTP étendu
    mail.starttls()  # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()

