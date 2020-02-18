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

class bdd_mysql:

	def __init__(self,adresse,utilisateur,password,name_databases,list_nutriment):

		self.config = configparser.ConfigParser()
		self.config.read('config.ini','utf8')

		if len(adresse) == 0 or len(utilisateur) == 0 or len(password) == 0 or len(name_databases) == 0:
			adresse = self.config.get('DEFAULT','host')
			utilisateur = self.config.get('DEFAULT','user')
			password = self.config.get('DEFAULT','password')
			name_databases = self.config.get('DEFAULT','database_name')

		self.host = adresse
		self.user = utilisateur
		self.pwd = password
		self.dataB = name_databases
		self.list_nutriment = list_nutriment

		self.msg_conn = conn_test(self.host,self.user,self.pwd,self.dataB)

	def req_sql(self,aff_class):
		titre = self.config.get('INTERACTION','categorie')
		init_affichage = aff_class
		list_seq = []
		cursor = self.msg_conn[0].cursor(buffered=True)
		seq_sql = "SELECT * FROM categories"
		cursor.execute(seq_sql)
		answer_bdd = cursor.fetchall()
		for answer in answer_bdd:
			inclure_list = str(answer[0]) + " - " + answer[1]
			list_seq.append(inclure_list)
		ask_nbr = init_affichage.aff_msg(list_seq,titre)
		seq_sql = "SELECT DISTINCT produits.id,produits.nom FROM produits,Tbl_jointure_categories_produits WHERE produits.id = Tbl_jointure_categories_produits.produits_id AND Tbl_jointure_categories_produits.categories_id = " + str(ask_nbr[0])+";"
		cursor.execute(seq_sql)
		answer_bdd = cursor.fetchall()
		list_seq = []
		for answer in answer_bdd:
			inclure_list = str(answer[0]) + " - " + answer[1]
			list_seq.append(inclure_list)
		titre = self.config.get('INTERACTION','produit') + " " + ask_nbr[1]
		ask_nbr = init_affichage.aff_msg(list_seq,titre)


	def msg_crea_bdd(self):

		if self.msg_conn[1] is None:
			self.print_succes = crea_bdd(self.msg_conn[0],self.list_nutriment)
			#return self.print_succes
		else:
			return self.msg_conn[1]

	def full_database(self,list_product,list_categorie,list_store):
		cursor = self.msg_conn[0].cursor(buffered=True)
		for categorie in list_categorie:
			seq_sql = "INSERT INTO Categories (nom) VALUES ('" + categorie + "')"
			cursor.execute(seq_sql)
			self.msg_conn[0].commit()
		for store in list_store:
			seq_sql = "INSERT INTO Vendeurs (nom) VALUES ('" + store + "')"
			cursor.execute(seq_sql)
			self.msg_conn[0].commit()
		for product in list_product:
			req_key_product = ''
			req_value_product = ''
			for key_product, value_product in product.items():
				insert_key = key_product.replace('-','_')
				copy_key = insert_key
				if insert_key == "categories":
					copy_key = 'jointure_categories_id'
					copy_value_categorie =  copy.deepcopy(value_product)
				if insert_key == "stores":
					copy_key = "jointure_vendeurs_id"
					copy_value_vendeurs =  copy.deepcopy(value_product)

				if insert_key.find('product') != -1:
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
						copy_key = 'nutri_score'
					
					if insert_key != "categories" and insert_key != "stores":
						req_key_product = req_key_product + copy_key + ","
						req_value_product = req_value_product + value_product + ','
					
			req_key_product = req_key_product[0:len(req_key_product)-1]
			req_value_product = req_value_product[0:len(req_value_product)-1]
			seq_sql = "INSERT INTO produits ("+req_key_product+") VALUES ("+req_value_product+");"
			cursor.execute(seq_sql)
			self.msg_conn[0].commit()
			last_id = cursor.lastrowid#cursor.execute("SELECT LAST_INSERT_ID() FROM produits;")
			for categorie in copy_value_categorie:
				seq_sql = "INSERT INTO Tbl_jointure_categories_produits (categories_id,produits_id) VALUES ("+str(categorie)+","+str(last_id)+");"
				cursor.execute(seq_sql)
			for vendeur in copy_value_vendeurs:
				seq_sql = "INSERT INTO Tbl_jointure_vendeurs_produits (vendeurs_id,produits_id) VALUES ("+str(vendeur)+","+str(last_id)+");"
				cursor.execute(seq_sql)
			self.msg_conn[0].commit()


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


def crea_bdd(conn,liste_nutriments):
	cursor = conn.cursor()
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
	
	conn.commit()
	print("Les tables ont bien été créés")
	

