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

class affichage:
	def __init__ (self):
		choix = 0
		clean()
		self.config = configparser.ConfigParser()
		self.config.read('config.ini','utf8')
		self.list_import_categorie = self.config.get('CONFIG','categories').split(',')
		self.list_ask_intro = self.config.get('INTERACTION','choix_begin').split(',')
		self.list_hello = self.config.get('INTERACTION','lancement').split(',')
		
		#self.ask_util = aff_intro(self.list_hello,list_ask_intro)

	def aff_intro(self):
		hello_word = self.list_hello[0] + '\n' + self.list_hello[1]
		print(hello_word)
		for text_intro in self.list_ask_intro:
			print(text_intro)

		ask_util = error_check(self.list_ask_intro)
		clean()
		return ask_util

	def aff_utilisation(self):
		liste_dict_produit = []
		req_produit = request()

		if self.ask_util == 1:
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

	def aff_msg(self,list_categories,titre):
		ask_all = []
		print(titre)
		for aff_result in list_categories:
			print(aff_result)
		ask_util = error_check(list_categories)
		ask_value = list_categories[ask_util]
		ask_all.append(ask_util)
		ask_all.append(ask_value)
		clean()
		return ask_all



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

def clean():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")
















