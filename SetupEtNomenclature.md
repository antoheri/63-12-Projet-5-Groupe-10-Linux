# Setup de l'environnement

## Installation de python

Normalement la plupart des distributions Linux intègrent python de base. Vous pouvez vérifier la version de python ainsi :

```bash
python3 --version
```

Si la commande ne fonctionne pas, voici comment installer python 3 :

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3
```

## Utilisation de GIT

Tuto utilisation de GIT : [Tuto GIT](https://www.w3schools.com/git/git_remote_getstarted.asp?remote=github)

## Utilisation du fichier login.env

Les informations de connexion au serveur FTP doivent être utilisées via des variables d'environnement. Sur votre machine locale, renommez le fichier ".env.example" en ".env" puis modifiez le avec les bonnes valeurs.
Celles-ci peuvent ensuite être récupérée et utilisée à l'aide de la bibliothèque "dotenv".

Tuto d'utilisation de dotenv : [Tuto dotenv](https://www.delftstack.com/fr/howto/python/dotenv-python/)

## Nomenclature

Variables:

- ma_variable

Constantes:

- MA_CONSTANTE
