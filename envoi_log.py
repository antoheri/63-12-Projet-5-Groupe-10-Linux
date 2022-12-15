import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
sendmail = os.environ.get('MAIL')
password = os.environ.get('MAIL_PASSWORD')

#username = nom d'utilisateur et le mail est le mail de celui qui modifie les utilisateurs ou les groupes
def new_user(username, mail):

    # Configuration SMTP
    host_smtp = "smtp.gmail.com"
    port_smtp = 587
    email_smtp = sendmail # email Gmail
    mdp_smtp = password  # mot de passe

    # Texte de l'email
    prenom = username
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour,\n\n le nouveau utilisateur {prenom} a été créé. \n\n{formule_p}'

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
    email_smtp = sendmail # email Gmail
    mdp_smtp = password  # mot de passe

    # Texte de l'email
    prenom = username
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f"Bonjour,\n\n l'utilisateur {prenom} a été supprimé. \n\n{formule_p}"

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
    email_smtp = sendmail # email Gmail
    mdp_smtp = password  # mot de passe

    # Texte de l'email
    prenom = username
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f"Bonjour,\n\n l'utilisateur {prenom} a été modifié. \n\n{formule_p}"

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
    email_smtp = sendmail # email Gmail
    mdp_smtp = password  # mot de passe

    #Texte de l'email
    
    group = groupname
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour,\n\n le nouveau groupe {group} a été créé. \n\n{formule_p}'

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
    email_smtp = sendmail # email Gmail
    mdp_smtp = password  # mot de passe

    # Texte de l'email
    
    group = groupname
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour,\n\n le groupe {group} a été supprimé. \n\n{formule_p}'

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
    email_smtp = sendmail # email Gmail
    mdp_smtp = password  # mot de passe
    # Texte de l'email
 
    group = groupname
    formule_p = "Meilleures salutations"
    email_destinataire = mail
    mail_content = f'Bonjour,\n\n le groupe {group} a été modifié. \n\n{formule_p}'

    # Création de l'objet mail
    mail = smtplib.SMTP(host_smtp, port_smtp)  # cette configuration fonctionne pour gmail
    mail.ehlo()  # protocole pour SMTP étendu
    mail.starttls()  # email crypté
    mail.login(email_smtp, mdp_smtp)
    mail.sendmail(email_smtp, email_destinataire, mail_content.encode('utf8'))
    mail.close()
