# -*-coding:Utf-8 -*

"""Ce Fichier contiendra la classe gérant l'affichage
"""

import sys
import os
import json
import requests
import copy
from class_requete import *
import configparser

class affichage:
	def __init__ (self):
		choix = 0

		self.config = configparser.ConfigParser()
		self.config.read('config.ini','utf8')
		self.list_import_categorie = self.config.get('CONFIG','categories').split(',')
		list_ask_intro = self.config.get('INTERACTION','choix_begin').split(',')
		list_hello = self.config.get('INTERACTION','lancement').split(',')
		hello_word = list_hello[0] + '\n' + list_hello[1]
		print(hello_word)
		for text_intro in list_ask_intro:
			print(text_intro)

		self.ask_util = error_check(list_ask_intro)
			

	def aff_utilisation(self):
		liste_dict_produit = []
		req_produit = request()
		if self.ask_util == 0:
			nw_bdd = req_produit.crea_bdd()
			liste_stores = req_produit.req_store()

			stores = aff_newliste(liste_stores,'stores')

			for x,cat_import in enumerate(self.list_import_categorie):
				req_result = req_produit.req_produit(cat_import)
				liste_produit = req_produit.crea_dictionnary(req_result,cat_import,x,stores)
				liste_dict_produit = liste_dict_produit + liste_produit
				
			aff_listeproduit = req_produit.dbl_listing(liste_dict_produit)		
			return liste_dict_produit

		elif self.ask_util == 1:
			req_categorie = req_produit.req_categorie()
			print(req_categorie)
			
	def aff_configbdd(self):
		list_aff = self.config.get('INTERACTION','config_bdd_title')
		list_config_bdd = self.config.get('INTERACTION','list_config_conn').split(',')
		print(list_aff)
		for text_config in list_config_bdd:
			param_config = input('Indiquer' + text_config + ': ')
			self.config.set('SAVE',text_config,param_config)

		self.config.write(open('config.ini','w'))
		writte_succed = "Configuration réussie"
		return writte_succed
			
def aff_newliste (req,field):
	liste_produit = []
	for value in req['products']:
		for key, value_products in value.items():
			if key.find(field) == 0:
				for categories in value_products:
					categories = categories.strip()
					if categories not in liste_produit and len(categories)>=3:
						liste_produit.append(categories)

	return liste_produit



def error_check(liste):
	while True:
		try:
			ask_util = int(input("Que voulez-vous faire ? "))
			if ask_util > len(liste):
				raise ValueError("Vous n'avez que ",len(liste)," choix")
			break
		except ValueError:
			print("La valeur saisie est invalide (ce n'est peut être pas un chiffre ou bien ce n'est pas un choix possible)")
	return ask_util














