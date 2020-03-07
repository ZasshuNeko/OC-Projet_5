# -*-coding:Utf-8 -*

"""Ce Fichier contiendra la gestion de la base
This File will contain the management of the database
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
    # Initialisation de l'objet connexion avec vérification sur la fonction conn_test
    # Initialization of the connection object with verification on the conn_test function
    def __init__(self, adresse,
                 utilisateur, password,
                 name_databases, list_nutriment):

        self.config = configparser.ConfigParser()
        self.config.read('config.ini', 'utf8')
        self.host = adresse
        self.user = utilisateur
        self.pwd = password
        self.dataB = name_databases
        self.list_nutriment = list_nutriment
        self.msg_conn = conn_test(self.host, self.user, self.pwd, self.dataB)

# Cette fonction créé les requêtes sql nécéssaire pour intéroger la base de
# donnée local et créé des listes de choix qu'il renvois vers la classe affichage
# This function creates the sql queries necessary to query the database
# local data and creates choice lists which it sends to the display class

    def req_sql(self, aff_class, end_prog):
        titre = self.config.get('INTERACTION', 'categorie')
        init_affichage = aff_class
        cursor = self.msg_conn[0].cursor(buffered=True)
        # Requête ramenant les catégories
        # Request bringing back the categories
        seq_sql = "SELECT * FROM categories"
        list_seq = dict_select(seq_sql,cursor)
        ask_nbr = init_affichage.aff_msg(list_seq[0], titre)
        ask_nbr[0] = ask_nbr[0] + 1
        # Requête pour les produits liés à la catégorie
        # sélectionné par l'utilisateur
        # Request for products linked to the category
        # selected by user
        seq_sql = "SELECT DISTINCT  " + \
                  self.config.get('CONFIG', 'sql_produit') + \
                  " FROM produits, Tbl_jointure_categories_produits WHERE \
                  produits.id = Tbl_jointure_categories_produits.produits_id \
                  AND Tbl_jointure_categories_produits.categories_id = " + \
                  str(ask_nbr[0])+";"
        list_seq = dict_select(seq_sql,cursor)
        titre = self.config.get('INTERACTION', 'produit') + " " + ask_nbr[1]
        ask_nbr_produit = init_affichage.aff_msg(list_seq[0], titre)
        index_answer_bdd = ask_nbr_produit[0]
        produit_list = list_seq[1]
        produit_select = produit_list[index_answer_bdd]
        produit_select_nutri_code = produit_select[2]
        list_substitut = list_sub(produit_list,self.config,produit_select_nutri_code)
        if list_substitut[0] != 0:
            result_substitut = list_substitut[1]
            # Requête pour ramener un substitut
            # Request to bring a substitute
            seq_sql = "SELECT * FROM produits WHERE \
                       produits.id = " + str(result_substitut[0])
            list_answer = list_select(seq_sql,cursor)
            # Requête permettant de trouver le vendeur du substitut
            # Query to find the seller of the substitute
            seq_sql = "SELECT DISTINCT  vendeurs.nom FROM vendeurs, \
                       Tbl_jointure_vendeurs_produits WHERE \
                       vendeurs.id = \
                       Tbl_jointure_vendeurs_produits.vendeurs_id \
                       AND Tbl_jointure_vendeurs_produits.produits_id = " + \
                      str(result_substitut[0])+";"
            list_answer_vendeurs = list_select(seq_sql,cursor)
            list_vendeur = ''
            for vendeur in list_answer_vendeurs:
                list_vendeur = list_vendeur + vendeur + '\n'
            if list_answer[18] is None:
                print_nutri_score = " non fournis par open food facts "
            else:
                print_nutri_score = list_answer[18]
            titre = "Voici votre substitut " + \
                    list_answer[1] + "\n Sont nutri_score : " + \
                    print_nutri_score + "\n Vous pouvez l'acheter :\n" + \
                    "- " + list_vendeur + \
                    "\n Suivez ce lien pour plus de détail : " + \
                    list_answer[19]
            ask_quitortry = init_affichage.aff_msg(list_substitut[0], titre)
        else:
            titre = "Aucun substitut trouvé"
            info_nosubstitut = self.config.get('INTERACTION',
                                               'nosubstitut').split(',')
            list_seq = {}
            for key, answer in enumerate(info_nosubstitut):
                list_seq[key] = answer
            ask_quitortry = init_affichage.aff_msg(list_seq, titre)
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
            # Requête permettant de sauvegarder le substitut
            # Request to save the substitute
            seq_sql = "INSERT INTO substitut_save \
                      (produit_id, substitut_id, date_time) \
                      VALUES (%s, %s, %s);"
            cursor.execute(seq_sql, list_insert)
            self.msg_conn[0].commit()
            init_affichage.aff_warning('Votre enregistrement a été réalisé')
            end_prog = True
        return end_prog

# Requête ramenant les recherches éffectuées
# Request bringing back the searches carried out

    def sql_take_substitut(self, aff_class, end_prog):
        list_produit = []
        list_substit = []
        list_log = []
        cursor = self.msg_conn[0].cursor(buffered=True)
        # Requête sélectionnant les produits sauvegardés dans la table
        # Query selecting the products saved in the table
        seq_sql = "SELECT substitut_save.date_time,produits.nom, \
                   produits.nutri_score FROM produits, \
                   substitut_save WHERE \
                   produits.id = substitut_save.produit_id;"
        cursor.execute(seq_sql)
        answer_bdd = cursor.fetchall()
        answer_bdd = list(answer_bdd)
        for answer in answer_bdd:
            insert_list_produit = answer[0].strftime("%d/%m/%Y %H:%M") + \
                                  " Produit sélectionné : " + answer[1] + \
                                  " nutri_score : " + answer[2]
            list_produit.append(insert_list_produit)
        # Requête ramenant les informations des produits substitués
        # Request bringing back the information of the substituted products
        seq_sql = "SELECT produits.nom, \
                   produits.nutri_score FROM \
                   produits,substitut_save WHERE \
                   produits.id = substitut_save.substitut_id;"
        cursor.execute(seq_sql)
        answer_bdd = cursor.fetchall()
        answer_bdd = list(answer_bdd)
        for answer in answer_bdd:
            insert_list_substitut = " Substitut trouvé : " + \
                                      answer[0] + " nutri_score : " + answer[1]
            list_substit.append(insert_list_substitut)
        titre = "Vos recherches"
        for key, items in enumerate(list_produit):
            insert_log = items + " ---> " + list_substit[key]
            titre = titre + "\n" + insert_log
        list_reponse = self.config.get('INTERACTION',
                                       'nosubstitut').split(',')
        list_seq = {}
        for key, answer in enumerate(list_reponse):
            list_seq[key] = answer
        init_affichage = aff_class
        ask_nbr_produit = init_affichage.aff_msg(list_seq, titre)

    def msg_crea_bdd(self, aff_mod):
        init_affichage = aff_mod
        if self.msg_conn[1] is None:
            self.print_succes = crea_bdd(self.msg_conn[0], self.list_nutriment)
            if self.print_succes[0]:
                init_affichage.aff_warning("Les tables ont bien été créés")
            else:
                init_affichage.aff_warning(self.print_succes[1])
                sys.exit(0)
        else:
            init_affichage.aff_warning(self.msg_conn[1])
            sys.exit(0)

    def full_database(self, list_product, list_categorie, list_store):
        # Récupération du mysql.connector
        # Retrieving mysql.connector"""
        cursor = self.msg_conn[0].cursor(buffered=True)
        # Permet le remplissage de la table catégorie
        # Allows filling of the category table"""
        list_insert_cat = []
        for categorie in list_categorie:
            list_insert_cat = []
            list_insert_cat.append(categorie)
            seq_sql = "INSERT INTO Categories (nom) VALUES (%s)"
            cursor.execute(seq_sql, list_insert_cat)
            self.msg_conn[0].commit()
        # Permet le remplissage de la table vendeurs
        # Allows filling of the vendors table
        list_insert_store = []
        for store in list_store:
            list_insert_store = []
            list_insert_store.append(store)
            seq_sql = "INSERT INTO Vendeurs (nom) VALUES (%s)"
            cursor.execute(seq_sql, list_insert_store)
            self.msg_conn[0].commit()
        # Permet le remplissage de la table produit
        # Allows filling of the product table

        for product in list_product:
            # Liste pour les injections sql
            # List for sql injections
            req_key_product = []
            req_value_product = []
            list_value_product = []
        # On parcourt le dictionnaire sélectionné
        # We browse the selected dictionary
            for key_product, value_product in product.items():
                # On ne prend pas en compte categories et vendeurs
                # We do not take into account categories and sellers
                if key_product != "categories" and key_product != "stores":
                    # On crée les listes pour l'injection sql
                    # We create the lists for sql injection
                    req_key_product.append(key_product)
                    list_value_product.append(value_product)
                    req_value_product.append('%s')
        # Passage des listes en str avec une séparation par la virgule
        # Passing lists in str with a comma separation
            bdd_key_product = ','.join(req_key_product)
            bdd_value_product = ','.join(req_value_product)
        # Injection des produits
        # Injection of products
            seq_sql = "INSERT INTO produits \
                      ("+bdd_key_product+") VALUES \
                      ("+bdd_value_product+");"
            cursor.execute(seq_sql, list_value_product)
            self.msg_conn[0].commit()
        # Récupération du dernier id dans la base
        # Retrieving the last id in the database
            last_id = cursor.lastrowid
        # Liste utilisé pour l'injection sql
        # List used for sql injection
            list_insert_table = []
        # Remplissage de la base de jointure catégories produits
        # Filling the product categories join base
            for categorie in product.get("categories"):
                list_insert_table = []
                list_insert_table.append(categorie)
                list_insert_table.append(last_id)
                seq_sql = "INSERT INTO Tbl_jointure_categories_produits \
                          (categories_id,produits_id) VALUES (%s,%s);"
                cursor.execute(seq_sql, list_insert_table)
        # Remplissage de la base de jointure vendeurs produits
        # Filling the product sellers join base
            for vendeur in product.get("stores"):
                list_insert_table = []
                list_insert_table.append(vendeur)
                list_insert_table.append(last_id)
                seq_sql = "INSERT INTO Tbl_jointure_vendeurs_produits \
                          (vendeurs_id,produits_id) VALUES (%s,%s);"
                cursor.execute(seq_sql, list_insert_table)
            self.msg_conn[0].commit()

# Test de la connexion à la base de donnée
# Test the connection to the database


def conn_test(adresse, utilisateur, password, name_databases):

    print_error = None
    try:
        conn = mysql.connector.connect(host=adresse,
                                       user=utilisateur, password=password,
                                       database=name_databases)
    except mysql.connector.Error as err:
        conn = "ERROR"
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print_error = "Vérifier le mot de passe ou l'utilisateur"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print_error = "La base n'existe pas"
        else:
            print_error = err
    return (conn, print_error)

# Création de la base de donnée selon le script sql
# Creation of the database according to the sql script


def crea_bdd(conn, liste_nutriments):

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
    return [check, error_msg]

# Lecture du script pour obtenir les commandes sql
# Reading the script to get sql commands

def script_read(nom_fichier):
    script_open = open(nom_fichier, 'r')
    sqlfile = script_open.read()
    script_open.close()
    sqlcommands = sqlfile.split(";")
    return sqlcommands

def dict_select(sql,cursor):
    list_seq = {}
    cursor.execute(sql)
    answer_bdd = cursor.fetchall()
    for key, answer in enumerate(answer_bdd):
        list_seq[key] = answer[1]
    return [list_seq,answer_bdd]

def list_select(sql,cursor):
    cursor.execute(sql)
    answer_bdd = cursor.fetchall()
    for answer in answer_bdd:
        list_answer = list(answer)
    return list_answer

def list_sub(produit_list,config,nutri_code):
    result_substitut = ""
    dict_nutriscore = {}
    dict_nutrimentO = {}
    dict_nutrimentT = {}
    dict_nutrimentTh = {}
    list_nutriment_sub = []
    for nutri_score in produit_list:
        if nutri_code is not None:
            if nutri_score[2] is not None:
                dict_nutriscore[nutri_score[0]] = nutri_score[2]
        else:
            if nutri_score[3] is not None:
                if nutri_score[3] is not None:
                    dict_nutrimentO[nutri_score[0]] = nutri_score[3]
    if len(dict_nutrimentO) != 0:
        min_keys = [k for k, x in dict_nutrimentO.items()
                    if not any(y < x for y in dict_nutrimentO.values())]
    else:
        min_keys = [k for k, x in dict_nutriscore.items()
                    if not any(y < x for y in dict_nutriscore.values())]
    random.shuffle(min_keys)
    for nutri_score in produit_list:
        if nutri_score[0] in min_keys:
            result_substitut = copy.deepcopy(nutri_score)
            break
    if len(result_substitut) != 0:
        info_substitut = config.get('INTERACTION',
                                         'substitut').split(',')
        list_seq = {}
        for key, answer in enumerate(info_substitut):
            list_seq[key] = answer
    return [list_seq,result_substitut]

