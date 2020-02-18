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
end_prog = True
#------------------------------------------------------
#Initialisation de la class requête et affichage
req_produit = request()
affichage_init = affichage()
# Demande à l'utilisateur de configurer la connexion de la base de donnée
if len(config.options('SAVE')) == 0:
	write_config = affichage_init.aff_configbdd()
	print(write_config)
#Test de la connexion à la base de donnée, création des tables, renvois d'un message de succes ou d'erreur
bdd_ini = bdd_mysql(config.get('SAVE','host'),config.get('SAVE','user'),config.get('SAVE','password'),config.get('SAVE','database_name'),list_import_nutriment)
while end_prog == True:
	answer_user = affichage_init.aff_intro()
	#------------------------------------------------------
	#Sélection des premier choix
	#Si 0 : Création des tables et chargement de la base de donnée
	if answer_user == 0:		
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
		bdd_ini.full_database(aff_listeproduit,list_import_categorie,liste_stores)
		print('done')
	elif answer_user == 1:
		req_dbt = bdd_ini.req_sql(affichage_init)
		#affichage_init.aff_msg(req_dbt)
	elif answer_user == 3:
		end_prog = False
		print("Aurevoir")
		#affichage_categorie = affichage_init.aff_utilisation()

	#print(affichage_categorie)



