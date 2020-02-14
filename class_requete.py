# -*-coding:Utf-8 -*

"""Ce Fichier contiendra la classe gérant les requêtes de l'API
"""

import sys
import os
import json
import copy
import re
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error
import requests
from bdd_mysql import bdd_mysql 

class request:

	def __init__(self):
		self.adress_api = "https://fr.openfoodfacts.org/cgi/search.pl?"
		self.final_api = "&action=process&json=1"
		self.liste_nutriments = ["energy_100g","energy-kcal_unit","salt_100g","salt_unit","sodium_100g","sodium_unit","proteins_100g","proteins_unit","carbohydrates_100g","carbohydrates_unit","fat_100g","fat_unit","sugars_100g","sugars_unit","saturated-fat_100g","saturated-fat_unit"]

	def req_categorie(self):
		tag = "search_tag=categories"
		req_api = self.adress_api + tag + self.final_api
		r = requests.get(req_api)
		result = json.loads(r.content)

		return result

	def req_produit(self,select_choice):
		tag = "search_terms="
		tag_bis = "&search_tag=categories"
		tag_choice = tag + '"' + select_choice + '"' + tag_bis
		req_api = self.adress_api + tag_choice + self.final_api
		r = requests.get(req_api)
		result = json.loads(r.content)
		return result

	def req_store(self):
		tag = "search_tag=stores"
		req_api = self.adress_api + tag + self.final_api
		r = requests.get(req_api)
		result = json.loads(r.content)

		list_store = crea_newliste(result,'stores')
		return list_store
		#return result

	def crea_dictionnary(self,req,cat_import,x,stores):
		dictionnary_produit = {}
		dict_produit = {}
		liste_dict_produit = []
		
		for value in req['products']:
			dictionnary_produit.clear()
			liste_field = crea_list_field(value)
			for empty_var in list(liste_field):
				if not value.get(empty_var):
					dictionnary_produit.clear()
					break
				else : 
					if empty_var == 'nutriments':
						
						for value_nutriment in value['nutriments']:
							for nutriments_empty in list(self.liste_nutriments):
								dictionnary_produit[nutriments_empty] = value['nutriments'].get(nutriments_empty)
					else:
						if empty_var.find('product') == 0:
							empty_var = 'product_name'
						dictionnary_produit[empty_var] = value.get(empty_var)	

			if dictionnary_produit:
				liste_stores = []
				dictionnary_produit["categories"] = [x]

				for key in value.keys():
					if key.find('stores') == 0:
						if len(value.get(key)) != 0:
							if type(value.get(key)) is not list:
								if len(value.get(key)) != 0:
									value_key = value.get(key).split(',')

							for store_select in stores:
								if store_select in value.get(key):
									if len(store_select) >= 3:
										liste_stores.append(stores.index(store_select))

							if len(liste_stores) == 0:
								for value_stores in value.get(key):
									if len(value_stores) >= 3:
										stores.append(value_stores)
										liste_stores.append(stores.index(value_stores))
				list_nodbl = []
				for data_stores in liste_stores:
					if not data_stores in list_nodbl:
						list_nodbl.append(data_stores)
				dictionnary_produit["stores"] = list_nodbl
				dict_insert = copy.deepcopy(dictionnary_produit)
				liste_dict_produit.append(dict_insert)
		return liste_dict_produit

	def dbl_listing(self,liste_produit):
		nw_liste_produit = []
		insert_value = True
		for x, nbr in enumerate(liste_produit):
			var_nom = nbr.get('product_name')
			if len(nw_liste_produit) == 0:
				nw_liste_produit.append(nbr)
			else:
				for value in nw_liste_produit:
					if var_nom == value.get('product_name'):
						insert_value == False

				if insert_value == True:
					nw_liste_produit.append(nbr)
				else:
					if not set(value.get('categories')).issubset(set(nbr.get('categories'))):
						val_manquante = [value for value in liste_cat_search if value not in liste_cat_find]
						nbr['categories']=nbr.get('categories') + val_manquante

		#print(nw_liste_produit)

	def crea_bdd(self):
		host = input("Indiquer l'adresse de la base de donnée (par défaut 'Localhost') : ")
		users = input("Indiquer l'utilisateur (par défaut 'root') : ")
		pwd = input("Mot de passe de votre base : ")
		dataB = input("Nom de votre base de donnée ? (par défaut 'oc_projet5)")

		bdd_ini = bdd_mysql(host,users,pwd,dataB,self.liste_nutriments)
		msg_bdd = bdd_ini.msg_crea_bdd()

		print(msg_bdd)

def crea_list_field(value):
	liste_field = ["nutriments"] #"product_name_fr",
	liste_field_test = ["nutrition_grade","product_name"]
	for field in liste_field_test:
		for key in value.keys():
			if field in key and value.get(key):
				liste_field.append(key)
				break
	return liste_field

def crea_newliste (req,field):
	liste_produit = []
	for value in req['products']:
		for key, value_products in value.items():
			if key.find(field) == 0:
				for categories in value_products:
					categories = categories.strip()
					if categories not in liste_produit and len(categories)>=3:
						liste_produit.append(categories)

	return liste_produit

