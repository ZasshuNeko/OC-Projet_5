OpenClassRooms - Projet 5

*##Version française*

I. Description
==============

Ce programme à pour but de renseigner un substitut plus sain à un aliment choisis par l'utilisateur
Il repose sur un jeu de donnée obtenue par l'API Open Food Facts.

II. Installation de python 3
============================

**Windows 10**
> Rendez-vous sur (https://python.org/downloads/)
> Télécharger la dernière version de python 3.X.X
> Installer la sur votre système

III. Installation de Git et copie du programme
==============================================

> Rendez-vous sur (https://git-scm.com/downloads)
> Télécharger la dernière version de git
> Installer cette dernière puis lancer l'application "Git Bash"

Copier le répertoire du programme avec la commnde : `git clone https://github.com/ZasshuNeko/OC-Projet_5.git`

IV. Installer et paramétrer Mysql
=================================

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
================

Le premier écran vous propose **5 choix**

* **Charger la base de donnée**

Cette option vous permet de lancer la configuration automatique des tables et d'importer le jeu de donnée venant de *Open Food Facts*

* **Quel aliment souhaitez vous remplacer**

Cette option permet de sélectionner la catégorie puis le produit en vu d'une substitution de l'aliment et ainsi obtenir un aliment plus sain.

* **Retrouver mes aliments susbtitués**

Si vous avez sauvegardé des recherche, cette option vous permet de les lister

* **Configurer la base de donnée**

Cette option vous permet de renseigner les données de connexion de votre base de donnée, mais vous pouvez le faire directement dans le fichier de configuration
*config.ini* 

* **Quitter**

Cette option vous permet de quitter le programme



*##English version*

I. Description
==============

This program aims to educate a healthier substitute for a food chosen by the user
It is based on a data set obtained by the Open Food Facts API.

II. Installation of python 3
============================

** Windows 10 **
> Go to (https://python.org/downloads/)
> Download the latest version of python 3.X.X
> Install it on your system

III. Installation of Gît and copy of the program
================================================

> Go to (https://git-scm.com/downloads)
> Download the latest version of git
> Install the latter then launch the "Git Bash" application

Copy the program directory with the command: `git clone https: // github.com / ZasshuNeko / OC-Projet_5.git`

IV. Install and configure Mysql
================================

> Go to (http://dev.mysql.com/downloads/mysql/#downloads)
> Then download the latest version of Mysql for your OS
> Once the installation is done and your administrator account created open the windows command prompt
`set PATH =% PATH%; chemin_vers_mysql_bin`
`mysql -u root -p`
> Enter your password then validate
> Before launching the program you must create your database
`CREATE DATABASE Name_of_your_base CHARACTER SET 'utf8';`
> You must then configure the program so that it can connect to your database
* Either you configure your database directly in the program, you just have to run it and refer to
the option ** Configure the database **
* Either in the application folder, open the "config.ini" file, in the "SAVE" section enter information like this:
`host = ** the address of your database **`
`user = ** User of your database **`
`password = ** user account password **`
`database_name = ** database name **`

V. Execute the program
=========================

Once the directory has been copied to the chosen location, open the command prompt and go to the directory
`cd chemin_du_repertoir`
Then execute the program by typing * OFF_main.py *

VI. The program
================

The first screen offers you ** 5 choices **

* **Charger la base de donnée**

This option allows you to launch the automatic configuration of the tables and to import the data set coming from * Open Food Facts *

* **Quel aliment souhaitez vous remplacer**

This option allows you to select the category then the product in view of a substitution of the food and thus obtain a healthier food.

* **Retrouver mes aliments susbtitués**

If you have saved searches, this option allows you to list them

* **Configurer la base de donnée**

This option allows you to enter the connection data for your database, but you can do so directly in the configuration file
Config.ini * *

* **Quitter**

This option allows you to exit the program