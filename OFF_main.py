# -*-coding:Utf-8 -*

"""Ce Fichier contiendra le fichier à exécuter pour lancer le programme
"""

import sys
import os
import json
import requests
from class_requete import *
from class_affichage import *
import configparser
from bdd_mysql import bdd_mysql 
#-------------------------------------
#Changement configParser et lecture du fichier config
config = configparser.ConfigParser()
config.read('config.ini','utf8')
#-----------------------------------------------------
#Chargement de la liste categorie et nutriment
list_import_categorie = config.get('CONFIG','categories').split(',')
list_import_nutriment = config.get('CONFIG','nutriments').split(',')
#------------------------------------------------------
liste_dict_produit = []
#------------------------------------------------------
#Initialisation de la class requête et affichage
req_produit = request()
affichage_init = affichage()
#------------------------------------------------------
#Sélection des premier choix
#Si 0 : Création des tables et chargement de la base de donnée
if affichage_init.ask_util == 0:
	# Si 0 : Demande à l'utilisateur de configurer la connexion de la base de donnée
	if len(config.options('SAVE')) == 0:
		write_config = affichage_init.aff_configbdd()
		print(write_config)
	#Test de la connexion à la base de donnée, création des tables, renvois d'un message de succes ou d'erreur
	bdd_ini = bdd_mysql(config.get('SAVE','host'),config.get('SAVE','user'),config.get('SAVE','password'),config.get('SAVE','database_name'),list_import_nutriment)
	bdd_ini.msg_crea_bdd()
	#Créer la liste des vendeurs
	liste_stores = req_produit.req_store()
	#Création d'une liste de dictionnaire constitué des produits à intégrer à la base
	for x,cat_import in enumerate(list_import_categorie):
		req_result = req_produit.req_produit(cat_import)
		liste_produit = req_produit.crea_dictionnary(req_result,cat_import,x,liste_stores)
		liste_dict_produit = liste_dict_produit + liste_produit
	#Retrait des doublons potentiel	
	aff_listeproduit = req_produit.dbl_listing(liste_dict_produit)		
	#print(liste_dict_produit)
	print('done')
	#affichage_categorie = affichage_init.aff_utilisation()

#print(affichage_categorie)



