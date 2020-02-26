OpenClassRooms - Projet 5

*##Version française*

I. Description
==============

Ce programme à pour but de renseigner un substitut plus sain à un aliment choisis par l'utilisateur
Il repose sur un jeu de donnée obtenue par l'API Open Food Facts.

II. Installation de python 3
============================

**Windows 10**
> Rendez-vous sur (python.org/downloads/)
> Télécharger la dernière version de python 3.X.X
> Installer la sur votre système

III. Installation de Git et copie du programme
==============================================

> Rendez-vous sur (https://git-scm.com/downloads)
> Télécharger la dernière version de git
> Installer cette dernière puis lancer l'application "Git Bash"

Copier le répertoire du programme avec la commnde : `git clone https://github.com/ZasshuNeko/OC-Projet_5.git`

IV. Installer et paramétrer Mysql

> Rendez-vous sur (http://dev.mysql.com/downloads/mysql/#downloads)
> Puis télécharger la dernière version de Mysql pour votre OS
> Une fois l'installation faite et votre compte administrateur créé ouvrez l'invite de commande windows
`set PATH=%PATH%;chemin_vers_mysql_bin`
`mysql -u root -p`
> Entrer votre mot de passe puis validez
> Avant de lancer le programme vous devez créer votre base de donnée
`CREATE DATABASE Nom_de_votre_base CHARACTER SET 'utf8';`
> Vous devez ensuite paramétrer le programme pour qu'il puisse se connecter à votre base de donnée
	* Soit vous configurez votre base de donée directement dans le programme, il vous suffit alors de l'exécuter et de vous référer à
	l'option **Configurer la base de donnée** 
	* Soit dans le dossier de l'application, ouvrez le fichier "config.ini", dans la partie "SAVE" entrer les informations comme cela :
	`host = **l'adresse de votre base de donnée**`
	`user = **Utilisateur de votre base de donnée**`
	`password = **mot de passe du compte utilisateur**`
	`database_name = **nom de la base de donnée**`

V. Executer le programme
=========================

Une fois le répertoire copié à l'emplacement choisis ouvrez l'invite de commande et placez-vous dans le répertoire
`cd chemin_du_repertoir`
Puis executer le programme en tapant *OFF_main.py*

VI. Le programme
===============

Le premier écran vous propose **5 choix**
* Charger la base de donnée

Cette option vous permet de lancer la configuration automatique des tables et d'importer le jeu de donnée venant de *Open Food Facts*

* Quel aliment souhaitez vous remplacer

Cette option permet de sélectionner la catégorie puis le produit en vu d'une substitution de l'aliment et ainsi obtenir un aliment plus sain.

* Retrouver mes aliments susbtitués

Si vous avez sauvegardé des recherche, cette option vous permet de les lister

* Configurer la base de donnée

Cette option vous permet de renseigner les données de connexion de votre base de donnée, mais vous pouvez le faire directement dans le fichier de configuration
*config.ini* 

* Quitter

Cette option vous permet de quitter le programme
