# -*-coding:Utf-8 -*

"""Ce Fichier contiendra la classe gérant les requêtes de l'API
This File will contain the class handling API requests
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
        self.list_nutrients = self.config.get(
                                                'CONFIG',
                                                'nutriments').split(',')

    # Ces modules permettent de créer une réponse jsons des
    # différentes demandes produits par l'API
    # These modules allow you to create a response to
    # different requests produced by the API

    # Permet de ramener les produits répondant aux catégories
    # indiqués en paramètre "select_choice"
    # Allows to bring back the products answering the categories
    # indicated in parameter "select_choice"

    def req_produit(self, select_choice):
        tag = "search_terms="
        tag_bis = "&search_tag=categories"
        tag_choice = tag + '"' + select_choice + '"' + tag_bis
        req_api = self.adress_api + tag_choice + self.final_api
        r = requests.get(req_api)
        result = json.loads(r.content)
        return result

    # Permet de ramener les différents vendeurs de Open Food Facts
    # Lets bring back the different sellers of Open Food Facts

    def req_store(self):

        tag = "search_tag=stores"
        req_api = self.adress_api + tag + self.final_api
        r = requests.get(req_api)
        result = json.loads(r.content)
        list_store = crea_newlist(result, 'stores')
        return list_store

    # Cette fonction créé le dictionnaire ou sera contenu
    # les produits de chaque catégories
    # This function creates the dictionary or will be contained
    # the products of each category

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
                                                         self.list_nutrients
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

    # Permet de retirer les doublons des
    # produits et de fusionner les catégories
    # Remove duplicates from products and merge
    # categories

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
        nw_list = dbl_newlist(list_produit_fusion, list_item_del)

        return nw_list


def dbl_newlist(list_base, list_item_del):

    nw_liste_insert = []
    for x, nbr in enumerate(list_base):
        if x not in list_item_del:
            nw_liste_insert.append(nbr)
    return nw_liste_insert


def dbl_fusionCat(list_del, list_keep):

    for items in list_keep:
        for items_del in list_del:
            if items.get('nom') == items_del.get('nom'):
                items['cat'] = items.get('cat') + items_del.get('cat')
    return list_keep


def crea_list_field(value):
    liste_field = ["nutriments", "url"]
    liste_field_test = ["grade", "product_name"]
    for field in liste_field_test:
        for key in value.keys():
            if field in key and value.get(key):
                liste_field.append(key)
                break
    return liste_field


def crea_newlist(req, field):

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
