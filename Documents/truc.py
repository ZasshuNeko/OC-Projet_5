[CONFIG]
categories = Eau,Boisson,Plats préparés,Petit-déjeuners,Produit à tartiner
nutriments = energy_100g,energy-kcal_unit,salt_100g,salt_unit,sodium_100g,sodium_unit,proteins_100g,proteins_unit,carbohydrates_100g,carbohydrates_unit,fat_100g,fat_unit,sugars_100g,sugars_unit,saturated-fat_100g,saturated-fat_unit,nutrition-score-fr_100g
sql_produit = produits.id,produits.nom,produits.nutri_score,produits.salt_100g,produits.fat_100g,produits.sugars_100g

[INTERACTION]
lancement = Bonjour Utilisateur,Veuillez choisir ce que vous désirez faire :
choix_begin = 0 - Charger la base de donnée,1 - Quel aliment souhaitez-vous remplacer ?,2 - Retrouver mes aliments substitués,3 - Configurer la base de donnée,4 - Quitter
config_bdd_title = Veuillez configurer votre connexion
list_config_conn = host,user,password,database_name
categorie = Veuillez entrer le chiffre correspondant à la catégories désirées
produit = Liste des produits de la catégorie :
substitut = Quitter,Accueil,Sauvegarder
nosubstitut = Quitter,Accueil

[SAVE]
host = localhost
user = root
password = ocsqlpassRooT*
database_name = ocprojetcinq

[AUTRES]
host = localhost
user = root
password = ocsqlpassRooT*
database_name = ocprojetcinq

		if len(adresse) == 0 or len(utilisateur) == 0 or len(password) == 0 or len(name_databases) == 0:
			adresse = self.config.get('DEFAULT','host')
			utilisateur = self.config.get('DEFAULT','user')
			password = self.config.get('DEFAULT','password')
			name_databases = self.config.get('DEFAULT','database_name')

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


				#inclure_list = str(answer[0]) + " - " + answer[1]


											for cat_find in nbr_entre_find:
												for cat_search in nbr_entre_search:	
													if cat_search != cat_find:
														nbr['categories']=liste_cat_find + cat_search
										else:
											if liste_cat_search != liste_cat_find:
												nbr['categories']=[liste_cat_find + liste_cat_search]	
											
										del liste_produit[index]
										if type(nbr.get('categories')) is list:
											list(set(nbr.get('categories')))


											nbr_tour = -1
		liste_index_del = []
		for x, nbr in enumerate(liste_produit):
			nbr_tour_comp = -1
			nbr_tour += 1
			for key,value in nbr.items():
				field = "products_name"
				if  key.find(field):
					var_nom = nbr.get(key)
					if var_nom is None:
						break
					for index,search in enumerate(liste_produit):
						nbr_tour_comp += 1
						if nbr_tour != nbr_tour_comp:
							for key_second,value_second in search.items():
								var_key = key_second

								if re.search(r"products_name",var_key) is not None :
									print(key_second,"++++++++++++++",field)
									var_search = search.get(key)
									if var_search is None:
										break
									if var_nom == var_search:
										liste_cat_search = search.get('categories')
										liste_cat_find = nbr.get('categories')
										if type(nbr.get('categories')) is list:
											liste_cat_find = nbr.get('categories')
										else:
											liste_cat_find = [nbr.get('categories')]

										if type(search.get('categories')) is list:
											liste_cat_search = search.get('categories')
										else :
											liste_cat_search = [search.get('categories')]

										if set(liste_cat_search).issubset(set(liste_cat_find)):
											liste_index_del.append(index)
										else:
											val_manquante = [value for value in liste_cat_search if value not in liste_cat_find]
											nbr['categories']=liste_cat_find + val_manquante
											liste_index_del.append(index)
		#del liste_produit[index]
		#print(liste_index_del)
		#print(liste_produit)
								#si liste alors traitement de comparaison par liste sinon simple comparaison
						if value.get(key) in stores:
							liste_stores.append(stores.index(value_stores))


									if len(host) <= 5:
			host = "localhost"
		if len(users) == 0:
			users = "root"
		if len(pwd) == 0:
			pwd = "ocsqlpassRooT*"
		if len(dataB) <= 6 :
			dataB = 'ocprojetcinq'

		try:

			conn = mysql.connector.connect(host=host,user=users,password=pwd,database=dataB)

		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Vérifier le mot de passe ou l'utilisateur")
			elif err.errno ==  errorcode.ER_BAD_DB_ERROR:
				print("La base n'existe pas")
			else:
				print(err)
		else:
			cursor = conn.cursor()
			field = ""
			for value in self.liste_nutriments:
				if value.find('unit') != 0:
					value = value.replace("-","_")
					nw_field = value + " CHAR(5),"
				else:
					nw_field = value + " SMALLINT UNSIGNED,"

				field = field + nw_field

			sql_sequence = "CREATE TABLE IF NOT EXISTS Produits (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL," + field + " nova_score TINYINT, nutri_score CHAR(5),categories_id SMALLINT UNSIGNED NOT NULL, vendeurs_id SMALLINT UNSIGNED NOT NULL, lien TEXT, PRIMARY KEY(id), CONSTRAINT fk_categorie_id FOREIGN KEY (categories_id) REFERENCES Categories(id), CONSTRAINT fk_vendeurs_id FOREIGN KEY (vendeurs_id) REFERENCES Vendeurs(id))ENGINE = InnoDB DEFAULT CHARSET=utf8;"
			print(sql_sequence)
			cursor.execute("CREATE TABLE IF NOT EXISTS Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL, PRIMARY KEY (id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
			cursor.execute("CREATE TABLE IF NOT EXISTS Vendeurs (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL, PRIMARY KEY (id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
			cursor.execute(sql_sequence)


		#while choix == 0:
			#self.ask_util = int(input("Que voulez-vous faire ? "))
			#if type(self.ask_util) != int:
				#print("entrer un chiffre")
			#elif type(self.ask_util) == int:
				#if self.ask_util > 3:
					#print("Vous n'avez que deux choix")
				#else:
					#choix = 1

							#self.liste_import_cat = ['Eau','Boisson','Plats préparés','Petit-déjeuners','Produit à tartiner']

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


					#req_key_product = req_key_product + copy_key + ","
					#req_value_product = req_value_product + value_product + ','
								#req_key_product = req_key_product[0:len(req_key_product)-1]
			#req_value_product = req_value_product[0:len(req_value_product)-1]

							"""if insert_key.find('product') != -1:
					copy_key = 'nom'
					value_product = value_product.replace("'","\\'")
					value_product = "\'" + value_product + "\'"

				if value_product is not None :
					if type(value_product) is not str :
						value_product = str(value_product)
					if insert_key.find('unit') != -1:
						value_product = "\'" + value_product + "\'"
					if insert_key.find('grade') != -1:
						if len(value_product) > 2:
							value_product = "'" + value_product[2] + "'"
						elif len(value_product) == 1:
							value_product = "'" + value_product + "'"
						copy_key = 'nutri_score'"""
										#insert_key = key_product.replace('-','_')

										"+str(categorie)+","+str(last_id)+"
										"+str(vendeur)+","+str(last_id)+"
													#seq_sql = "INSERT INTO Categories (nom) VALUES ('" + categorie + "')"


													field = ""
	for value in liste_nutriments:
		if value.find('unit') != -1:
			value = value.replace("-","_")
			nw_field = value + " CHAR(5),"
		else:
			value = value.replace("-","_")
			nw_field = value + " DECIMAL(7,2) UNSIGNED,"

		field = field + nw_field

	sql_sequence = "CREATE TABLE IF NOT EXISTS Produits (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL," + field + " nova_score TINYINT, nutri_score CHAR(5), lien TEXT, PRIMARY KEY(id))ENGINE = InnoDB DEFAULT CHARSET=utf8;"#, CONSTRAINT fk_categorie_id FOREIGN KEY (categories_id) REFERENCES Categories(id), CONSTRAINT fk_vendeurs_id FOREIGN KEY (vendeurs_id) REFERENCES Vendeurs(id)
	cursor.execute("CREATE TABLE IF NOT EXISTS Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL, PRIMARY KEY (id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute("CREATE TABLE IF NOT EXISTS Vendeurs (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL, PRIMARY KEY (id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute(sql_sequence)
	cursor.execute("CREATE TABLE IF NOT EXISTS Substitut_save (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, produit_id SMALLINT UNSIGNED NOT NULL,date_time DATETIME NOT NULL, PRIMARY KEY (id),CONSTRAINT fk_produit_id FOREIGN KEY (produit_id) REFERENCES Produits(id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute("CREATE TABLE IF NOT EXISTS Tbl_jointure_categories_produits (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, categories_id SMALLINT UNSIGNED NOT NULL,produits_id SMALLINT UNSIGNED NOT NULL, PRIMARY KEY (id),CONSTRAINT fk_categories_id FOREIGN KEY (categories_id) REFERENCES Categories(id), CONSTRAINT fk_produits_categories_id FOREIGN KEY (produits_id) REFERENCES Produits(id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute("CREATE TABLE IF NOT EXISTS Tbl_jointure_vendeurs_produits (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, vendeurs_id SMALLINT UNSIGNED NOT NULL,produits_id SMALLINT UNSIGNED NOT NULL, PRIMARY KEY (id),CONSTRAINT fk_vendeurs_id FOREIGN KEY (vendeurs_id) REFERENCES Vendeurs(id),CONSTRAINT fk_produits_vendeurs_id FOREIGN KEY (produits_id) REFERENCES Produits(id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	

				if produit_select_nutri_code is not None and self.dict_nutri_score.get(nutri_score[2]) is not None :
				if self.dict_nutri_score.get(nutri_score[2]) < produit_select_nutri_code:
					result_substitut = copy.deepcopy(nutri_score)

		if len(result_substitut) == 0:
			for nutri_score in answer_bdd:
				if produit_select_nutri_code is not None and self.dict_nutri_score.get(nutri_score[2]) is not None :
					if nutri_score[2] == produit_select_nutri_code:
						if nutri_score[3] < produit_select[3] or nutri_score[4] < produit_select[4] or nutri_score[5] < produit_select[5]:
							result_substitut = copy.deepcopy(nutri_score)
				else:
					print(nutri_score[3])
					if float(nutri_score[3]) < float(produit_select[3]) or float(nutri_score[4]) < produit_select[4] or nutri_score[5] < produit_select[5]:
							result_substitut = copy.deepcopy(nutri_score)


	def crea_bdd(self):
		host = input("Indiquer l'adresse de la base de donnée (par défaut 'Localhost') : ")
		users = input("Indiquer l'utilisateur (par défaut 'root') : ")
		pwd = input("Mot de passe de votre base : ")
		dataB = input("Nom de votre base de donnée ? (par défaut 'oc_projet5)")

		bdd_ini = bdd_mysql(host,users,pwd,dataB,self.liste_nutriments)
		msg_bdd = bdd_ini.msg_crea_bdd()

		print(msg_bdd)
	def req_categorie(self):
		tag = "search_tag=categories"
		req_api = self.adress_api + tag + self.final_api
		r = requests.get(req_api)
		result = json.loads(r.content)
		return result

		def aff_utilisation(self):
		liste_dict_produit = []
		req_produit = request()
		if self.ask_util == 1:
			req_categorie = req_produit.req_categorie()
			print(req_categorie)


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

def main():
"""----------------------------------------------------
Changement configParser et lecture du fichier config"""
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
	#Test de la connexion à la base de donnée, création des tables, renvois d'un message de succes ou d'erreur
	bdd_ini = bdd_mysql(config.get('SAVE','host'),config.get('SAVE','user'),config.get('SAVE','password'),config.get('SAVE','database_name'),list_import_nutriment)
	#Si la connexion ne se fait pas, remonter l'erreur puis fermer le programme
	if bdd_ini.msg_conn[1] is not None:
		init_affichage.aff_warning(bdd_ini.msg_conn[1])
		sys.exit(0)
	while end_prog == True:
		answer_user = affichage_init.aff_intro()
		#------------------------------------------------------
		#Sélection des premier choix
		#Si 0 : Création des tables et chargement de la base de donnée
		if answer_user == 0:		
			bdd_ini.msg_crea_bdd(affichage_init)
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
		# Si 1 : Lance la recherche de substitut
		elif answer_user == 1:
			req_dbt = bdd_ini.req_sql(affichage_init,end_prog)
			end_prog = req_dbt
		#si 2 : Recherche les substituts déjà trouvé
		elif answer_user == 2:
			req_take_substitut = bdd_ini.sql_take_substitut(affichage_init,end_prog)
		#si 3 : Permet de configurer la connexion de la base de donnée dans le programme
		elif answer_user == 3:
			write_config = affichage_init.aff_configbdd()
		#si 4 : Quitte le programme
		elif answer_user == 4:
			end_prog = False

	affichage_init.aff_end()	

if __name__=='__main__' : main()


# -*-coding:Utf-8 -*

"""Ce Fichier contiendra la classe gérant l'affichage
"""

import sys
import os
import json
import requests
import copy
from class_requete import *
from bdd_mysql import bdd_mysql 
import configparser
import platform
import codecs

class affichage:
	def __init__ (self):
		choix = 0
		clean()
		self.config = configparser.ConfigParser()
		self.config.read('config.ini','utf8')
		self.list_import_categorie = self.config.get('CONFIG','categories').split(',')
		self.list_ask_intro = self.config.get('INTERACTION','choix_begin').split(',')
		self.list_hello = self.config.get('INTERACTION','lancement').split(',')
#Affiche le message d'introduction du programme
	def aff_intro(self):
		clean()
		hello_word = self.list_hello[0] + '\n' + self.list_hello[1]
		print(hello_word)
		for text_intro in self.list_ask_intro:
			print(text_intro)
		ask_util = error_check(self.list_ask_intro)
		clean()
		return ask_util
#Affiche et enregistre les configurations de la base de donnée
	def aff_configbdd(self):
		list_aff = self.config.get('INTERACTION','config_bdd_title')
		list_config_bdd = self.config.get('INTERACTION','list_config_conn').split(',')
		print(list_aff)
		for text_config in list_config_bdd:
			param_config = input('Indiquer ' + text_config + ' : ')
			self.config.set('SAVE',text_config,param_config)
		self.config.write(codecs.open('config.ini','w','utf8'))
		print("Configuration réussie")
#Affiche un choix utilisateurs
	def aff_msg(self,list_categories,titre):
		ask_all = []
		print(titre)
		for key,aff_result in list_categories.items():
			print(key, " - ",aff_result)
		ask_util = error_check(list_categories)
		ask_value = list_categories[ask_util]
		ask_all.append(ask_util)
		ask_all.append(ask_value)
		clean()
		return ask_all
#Affiche le message de fin
	def aff_end(self):
		print("Merci d'avoir utiliser mon programme, à bientôt sur un prochain projet OpenClassrooms")
#Affiche un message d'erreur
	def aff_warning(self,warning):
		clean()
		print(warning)
#Permet de vérifier qu'un choix fait par l'utilisateur est bon		
def error_check(liste):
	while True:
		try:
			ask_util = int(input("Que voulez-vous faire ? "))
			if ask_util > len(liste)-1: #or ask_util == 0:
				raise ValueError("Vous n'avez que ",len(liste)," choix")
			break
		except ValueError:
			print("La valeur saisie est invalide (ce n'est peut être pas un chiffre ou bien ce n'est pas un choix possible)")
	return ask_util
#Permet de nétoyer l'interface
def clean():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")




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
import configparser
from mysql.connector import errorcode
from mysql.connector.errors import Error
import requests


class request:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', 'utf8')
        self.adress_api = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.final_api = "&action=process&json=1"
        self.liste_nutriments = self.config.get(
                                                'CONFIG',
                                                'nutriments').split(',')

    """ Ces modules permettent de créer une réponse jsons des
    différentes demandes produits par l'API

    Permet de ramener les produits répondant aux catégories
    indiqués en paramètre "select_choice" """

    def req_produit(self, select_choice):
        tag = "search_terms="
        tag_bis = "&search_tag=categories"
        tag_choice = tag + '"' + select_choice + '"' + tag_bis
        req_api = self.adress_api + tag_choice + self.final_api
        r = requests.get(req_api)
        result = json.loads(r.content)
        return result

    # Permet de ramener les différents vendeurs de Open Food Facts

    def req_store(self):

        tag = "search_tag=stores"
        req_api = self.adress_api + tag + self.final_api
        r = requests.get(req_api)
        result = json.loads(r.content)
        list_store = crea_newliste(result, 'stores')
        return list_store

    """ Ce module créé le dictionnaire ou sera contenu
    les produits de chaque catégories"""

    def crea_dictionnary(self, req, cat_import, x, stores):
        dictionnary_produit = {}
        dict_produit = {}
        liste_dict_produit = []
        x = x + 1
        for value in req['products']:
            dictionnary_produit.clear()
            liste_field = crea_list_field(value)
            for empty_var in list(liste_field):
                if not value.get(empty_var):
                    dictionnary_produit.clear()
                    break
                else:
                    if empty_var == 'nutriments':
                        for value_nutriment in value['nutriments']:
                            for nutriments_empty in list(
                                                         self.liste_nutriments
                                                         ):
                                insert_key = nutriments_empty.replace('-', '_')
                                if insert_key.find('nutrition_score_fr') != -1:
                                    insert_key = 'nutri_score'
                                dictionnary_produit[insert_key] = value['nutriments'].get(nutriments_empty)
                    elif empty_var.find('product') == 0:
                        empty_var = 'product_name'
                        key_var = 'nom'
                        dictionnary_produit[key_var] = value.get(empty_var)
                    elif empty_var.find('url') != -1:
                        empty_var = 'url'
                        key_var = 'lien'
                        dictionnary_produit[key_var] = value.get(empty_var)
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
                                        liste_stores.append(stores
                                                            .index(store_select))
                            if len(liste_stores) == 0:
                                for value_stores in value.get(key):
                                    if len(value_stores) >= 3:
                                        stores.append(value_stores)
                                        liste_stores.append(stores
                                                            .index(value_stores))
                list_nodbl = []
                for data_stores in liste_stores:
                    data_stores = data_stores + 1
                    if data_stores not in list_nodbl:
                        list_nodbl.append(data_stores)
                dictionnary_produit["stores"] = list_nodbl
                dict_insert = copy.deepcopy(dictionnary_produit)
                liste_dict_produit.append(dict_insert)
        return liste_dict_produit

    """ Permet de retirer les doublons des
    produits et de fusionner les catégories"""

    def dbl_listing(self, liste_produit):
        dict_item_keep = {}
        dict_item_del = {}
        list_item_keep = []
        list_item_del = []
        fingerprints = set()
        for index, x in enumerate(liste_produit):
            fingerprint = x.get('nom')
            if fingerprint is not None:
                if fingerprint not in fingerprints:
                    yield x
                    fingerprints.add(fingerprint)
                    dict_item_keep['nom'] = x.get('nom')
                    dict_item_keep['cat'] = x.get('categories')
                    dict_item_keep['index'] = index
                    list_item_keep.append(dict_item_keep)

                else:
                    dict_item_del['nom'] = x.get('nom')
                    dict_item_del['cat'] = x.get('categories')
                    dict_item_del['index'] = index
                    list_item_del.append(dict_item_del)

        list_produit_fusion = dbl_fusionCat(list_item_del, list_item_keep)
        nw_list = dbl_newlist(list_produit_fusion,list_item_del)

        return nw_list

        

def dbl_newlist(list_base,list_item_del):
    nw_liste_insert = []
    for x, nbr in enumerate(list_base):
        if not x in list_item_del:
            nw_liste_insert.append(nbr)
    return nw_liste_insert

def dbl_fusionCat(list_del,list_keep):
    for items in list_keep:
        for items_del in list_del:
            if items.get('nom') == items_del.get('nom'):
                items['cat'] = items.get('cat') + items_del.get('cat')
    return list_keep


def crea_list_field(value):
    liste_field = ["nutriments", "url"]
    liste_field_test = ["grade", "product_name"]#product_name
    for field in liste_field_test:
        for key in value.keys():
            if field in key and value.get(key):
                liste_field.append(key)
                break
    return liste_field


def crea_newliste(req, field):

    liste_produit = []
    for value in req['products']:
        for key, value_products in value.items():
            if key.find(field) == 0:
                for categories in value_products:
                    categories = categories.strip()
                    if categories not in liste_produit \
                       and len(categories) >= 3:
                        liste_produit.append(categories)
    return liste_produit

# -*-coding:Utf-8 -*

"""Ce Fichier contiendra la gestion de la base
"""

import sys
import os
import json
import configparser
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error
from class_affichage import *
import requests
import copy
import datetime
import random

class bdd_mysql:

	def __init__(self,adresse,utilisateur,password,name_databases,list_nutriment):
		
		self.config = configparser.ConfigParser()
		self.config.read('config.ini','utf8')

		self.host = adresse
		self.user = utilisateur
		self.pwd = password
		self.dataB = name_databases
		self.list_nutriment = list_nutriment

		self.msg_conn = conn_test(self.host,self.user,self.pwd,self.dataB)

	def req_sql(self,aff_class,end_prog):
		titre = self.config.get('INTERACTION','categorie')
		init_affichage = aff_class
		list_seq = {}
		cursor = self.msg_conn[0].cursor(buffered=True)
		seq_sql = "SELECT * FROM categories"
		cursor.execute(seq_sql)
		answer_bdd = cursor.fetchall()
		for key,answer in enumerate(answer_bdd):
			list_seq[key] = answer[1]
		ask_nbr = init_affichage.aff_msg(list_seq,titre)
		ask_nbr[0] = ask_nbr[0] + 1
		seq_sql = "SELECT DISTINCT  " + self.config.get('CONFIG','sql_produit') +" FROM produits,Tbl_jointure_categories_produits WHERE produits.id = Tbl_jointure_categories_produits.produits_id AND Tbl_jointure_categories_produits.categories_id = " + str(ask_nbr[0])+";"
		cursor.execute(seq_sql)
		answer_bdd = cursor.fetchall()
		list_seq = {}
		for key,answer in enumerate(answer_bdd):
			list_seq[key] = answer[1]
		titre = self.config.get('INTERACTION','produit') + " " + ask_nbr[1]
		ask_nbr_produit = init_affichage.aff_msg(list_seq,titre)
		index_answer_bdd = ask_nbr_produit[0]
		produit_select = answer_bdd[index_answer_bdd]
		produit_select_nutri_code = produit_select[2]
		result_substitut = ""
		dict_nutriscore = {}
		dict_nutrimentO = {}
		dict_nutrimentT = {}
		dict_nutrimentTh = {}
		list_nutriment_sub = []
		for nutri_score in answer_bdd:
			if produit_select_nutri_code is not None:
				if nutri_score[2] is not None:
					dict_nutriscore[nutri_score[0]] = nutri_score[2]
			else:
				if nutri_score[3] is not None:
					if nutri_score[3] is not None:
						dict_nutrimentO[nutri_score[0]] = nutri_score[3]
		
		if len(dict_nutrimentO) != 0:
			min_keys = [k for k,x in dict_nutrimentO.items() if not any(y < x for y in dict_nutrimentO.values())]
		else:
			min_keys = [k for k,x in dict_nutriscore.items() if not any(y < x for y in dict_nutriscore.values())]			
		random.shuffle(min_keys)
		for nutri_score in answer_bdd:
			if nutri_score[0] in min_keys:
				result_substitut = copy.deepcopy(nutri_score)
				break

		if len(result_substitut) != 0:
			info_substitut = self.config.get('INTERACTION','substitut').split(',')
			list_seq = {}
			for key,answer in enumerate(info_substitut):
				list_seq[key] = answer
			seq_sql = "SELECT * FROM produits WHERE produits.id = " + str(result_substitut[0])
			cursor.execute(seq_sql)
			answer_substitut = cursor.fetchall()
			for answer in answer_substitut:
				list_answer = list(answer)
			seq_sql = "SELECT DISTINCT  vendeurs.nom FROM vendeurs,Tbl_jointure_vendeurs_produits WHERE vendeurs.id = Tbl_jointure_vendeurs_produits.vendeurs_id AND Tbl_jointure_vendeurs_produits.produits_id = " + str(result_substitut[0])+";"
			cursor.execute(seq_sql)
			answer_vendeur = cursor.fetchall()
			for answer in answer_vendeur:
				list_answer_vendeurs = list(answer)
			list_vendeur = ''
			for vendeur in list_answer_vendeurs:
				list_vendeur = list_vendeur + vendeur + '\n'

			if list_answer[19] is None :
				print_nutri_score = " non fournis par open food facts "
			else:
				print_nutri_score = list_answer[19]

			titre = "Voici votre substitut " + list_answer[1] + "\n Sont nutri_score : " + print_nutri_score + "\n Vous pouvez l'acheter :\n" + "- " + list_vendeur + "\n Suivez ce lien pour plus de détail : " + list_answer[20]
			ask_quitortry = init_affichage.aff_msg(list_seq,titre)
		else:
			titre = "Aucun substitut trouvé"
			info_nosubstitut = self.config.get('INTERACTION','nosubstitut').split(',')
			list_seq = {}
			for key,answer in enumerate(info_nosubstitut):
				list_seq[key] = answer
			ask_quitortry = init_affichage.aff_msg(list_seq,titre)

		if ask_quitortry[0] == 0:
			end_prog = False
		elif ask_quitortry[0] == 1:
			end_prog = True
		elif ask_quitortry[0] == 2:
			date_save = datetime.datetime.now()
			list_insert = []
			list_insert.append(produit_select[0])
			list_insert.append(list_answer[0])
			list_insert.append(date_save)
			print(list_insert)
			seq_sql = "INSERT INTO substitut_save (produit_id,substitut_id,date_time) VALUES (%s,%s,%s);"
			cursor.execute(seq_sql,list_insert)
			self.msg_conn[0].commit()
			init_affichage.aff_warning('Votre enregistrement a été réalisé')
			end_prog = True

		return end_prog

	def sql_take_substitut(self,aff_class,end_prog):
		list_produit = []
		list_substit = []
		list_log = []
		cursor = self.msg_conn[0].cursor(buffered=True)
		seq_sql = "SELECT substitut_save.date_time,produits.nom, produits.nutri_score FROM produits,substitut_save WHERE produits.id = substitut_save.produit_id;"
		cursor.execute(seq_sql)
		answer_bdd = cursor.fetchall()
		answer_bdd = list(answer_bdd)
		for answer in answer_bdd:
			insert_list_produit = answer[0].strftime("%d/%m/%Y %H:%M") + " Produit sélectionné : " + answer[1] + " nutri_score : " + answer[2]
			list_produit.append(insert_list_produit)
		seq_sql = "SELECT produits.nom, produits.nutri_score FROM produits,substitut_save WHERE produits.id = substitut_save.substitut_id;"
		cursor.execute(seq_sql)
		answer_bdd = cursor.fetchall()
		answer_bdd = list(answer_bdd)
		for answer in answer_bdd:
			insert_list_substitut = " Substitut trouvé : " + answer[0] + " nutri_score : " + answer[1]
			list_substit.append(insert_list_substitut)	

		titre = "Vos recherches"

		for key,items in enumerate(list_produit):
			insert_log = items + "--->" + list_substit[key]
			titre = titre + "\n" + insert_log
		list_reponse =  self.config.get('INTERACTION','nosubstitut').split(',')
		list_seq = {}
		for key,answer in enumerate(list_reponse):
			list_seq[key] = answer
		init_affichage = aff_class
		ask_nbr_produit = init_affichage.aff_msg(list_seq,titre)


	def msg_crea_bdd(self,aff_mod):
		init_affichage = aff_mod
		if self.msg_conn[1] is None:
			self.print_succes = crea_bdd(self.msg_conn[0],self.list_nutriment)
			if self.print_succes[0] == True:
				init_affichage.aff_warning("Les tables ont bien été créés")
			else:
				init_affichage.aff_warning(self.print_succes[1])
				sys.exit(0)
		else:
			init_affichage.aff_warning(self.msg_conn[1])
			sys.exit(0)

	def full_database(self,list_product,list_categorie,list_store):
		#Récupération du mysql.connector
		cursor = self.msg_conn[0].cursor(buffered=True)
		#Permet le remplissage de la table catégorie
		list_insert_cat = []
		for categorie in list_categorie:
			list_insert_cat = []
			list_insert_cat.append(categorie)
			seq_sql = "INSERT INTO Categories (nom) VALUES (%s)"
			cursor.execute(seq_sql,list_insert_cat)
			self.msg_conn[0].commit()
		#Permet le remplissage de la table vendeurs
		list_insert_store = []
		for store in list_store:
			list_insert_store = []
			list_insert_store.append(store)
			seq_sql = "INSERT INTO Vendeurs (nom) VALUES (%s)"
			cursor.execute(seq_sql,list_insert_store)
			self.msg_conn[0].commit()
		#Permet le remplissage de la table produit
		for product in list_product:
		#Liste pour les injections sql
			req_key_product = []
			req_value_product = []
			list_value_product = []
		#On parcourt le dictionnaire sélectionné
			for key_product, value_product in product.items():
		#On ne prend pas en compte categories et vendeurs
				if key_product != "categories" and key_product != "stores":
		#On crée les listes pour l'injection sql
					req_key_product.append(key_product)
					list_value_product.append(value_product)
					req_value_product.append('%s')
		#Passage des listes en str avec une séparation par la virgule
			bdd_key_product = ','.join(req_key_product)
			bdd_value_product = ','.join(req_value_product)
		#Injection du produit
			seq_sql = "INSERT INTO produits ("+bdd_key_product+") VALUES ("+bdd_value_product+");"
			cursor.execute(seq_sql,list_value_product)
			self.msg_conn[0].commit()
		#Récupération du dernier id dans la base
			last_id = cursor.lastrowid
		#Liste utilisé pour l'injection sql
			list_insert_table = []
		#Remplissage de la base de jointure catégories produits
			for categorie in product.get("categories"):
				list_insert_table = []
				list_insert_table.append(categorie)
				list_insert_table.append(last_id)
				seq_sql = "INSERT INTO Tbl_jointure_categories_produits (categories_id,produits_id) VALUES (%s,%s);"
				cursor.execute(seq_sql, list_insert_table)
		#Remplissage de la base de jointure vendeurs produits
			for vendeur in product.get("stores"):
				list_insert_table = []
				list_insert_table.append(vendeur)
				list_insert_table.append(last_id)
				seq_sql = "INSERT INTO Tbl_jointure_vendeurs_produits (vendeurs_id,produits_id) VALUES (%s,%s);"
				cursor.execute(seq_sql,list_insert_table)
			self.msg_conn[0].commit()

#Test de la connexion à la base de donnée
def conn_test(adresse,utilisateur,password,name_databases):
	print_error = None
	try:
		conn = mysql.connector.connect(host=adresse,user=utilisateur,password=password,database=name_databases)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print_error = "Vérifier le mot de passe ou l'utilisateur"
		elif err.errno ==  errorcode.ER_BAD_DB_ERROR:
			print_error = "La base n'existe pas"
		else:
			print_error = err
	return (conn,print_error)
#Création de la base de donnée selon le script sql
def crea_bdd(conn,liste_nutriments):
	cursor = conn.cursor()
	sqlcommands = script_read('script_sql.sql')
	check = True
	error_msg = ""
	for command in sqlcommands:
		try:
			cursor.execute(command)
		except mysql.connector.Error as err:
			error_msg = err.msg
			check = False
	conn.commit()
	return [check,error_msg]
#Lecture du script pour obtenir les commandes sql	
def script_read(nom_fichier):
	script_open = open(nom_fichier,'r')
	sqlfile = script_open.read()
	script_open.close()
	sqlcommands = sqlfile.split(";")
	return sqlcommands





