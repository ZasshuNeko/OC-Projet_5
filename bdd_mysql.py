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
import requests

class bdd_mysql:

	def __init__(self,adresse,utilisateur,password,name_databases,list_nutriment):

		config = configparser.ConfigParser()
		config.read('config.ini')

		if len(adresse) == 0 or len(utilisateur) == 0 or len(password) == 0 or len(name_databases) == 0:
			adresse = config.get('DEFAULT','host')
			utilisateur = config.get('DEFAULT','user')
			password = config.get('DEFAULT','password')
			name_databases = config.get('DEFAULT','database_name')

		self.host = adresse
		self.user = utilisateur
		self.pwd = password
		self.dataB = name_databases
		self.list_nutriment = list_nutriment

		self.msg_conn = conn_test(self.host,self.user,self.pwd,self.dataB)

	def msg_crea_bdd(self):

		if self.msg_conn[1] is None:
			self.print_succes = crea_bdd(self.msg_conn[0],self.list_nutriment)
			return self.print_succes
		else:
			return self.msg_conn[1]
		

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
			nw_field = value + " DECIMAL(5,2) UNSIGNED,"

		field = field + nw_field

	sql_sequence = "CREATE TABLE IF NOT EXISTS Produits (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL," + field + " nova_score TINYINT, nutri_score CHAR(5),categories_id SMALLINT UNSIGNED NOT NULL, vendeurs_id SMALLINT UNSIGNED NOT NULL, lien TEXT, PRIMARY KEY(id), CONSTRAINT fk_categorie_id FOREIGN KEY (categories_id) REFERENCES Categories(id), CONSTRAINT fk_vendeurs_id FOREIGN KEY (vendeurs_id) REFERENCES Vendeurs(id))ENGINE = InnoDB DEFAULT CHARSET=utf8;"
	cursor.execute("CREATE TABLE IF NOT EXISTS Substitut_save (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, produit_id SMALLINT UNSIGNED NOT NULL,date_time DATETIME NOT NULL, PRIMARY KEY (id),CONSTRAINT fk_produit_id FOREIGN KEY (produit_id) REFERENCES Produits(id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute("CREATE TABLE IF NOT EXISTS Categories (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL, PRIMARY KEY (id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute("CREATE TABLE IF NOT EXISTS Vendeurs (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, nom TEXT NOT NULL, PRIMARY KEY (id))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
	cursor.execute(sql_sequence)

	print("Les tables ont bien été créés")

