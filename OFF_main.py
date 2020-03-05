# -*-coding:Utf-8 -*

"""Ce Fichier contiendra le fichier à exécuter pour lancer le programme
This File will contain the file to execute to launch the program
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
    # ----------------------------------------------------
    # Changement configParser et lecture du fichier config
    # Change configParser and read the config file
    config = configparser.ConfigParser()
    config.read('config.ini', 'utf8')
    # -----------------------------------------------------
    # Chargement de la liste categorie et nutriment
    # Loading the category and nutrient list
    list_import_category = config.get('CONFIG', 'categories').split(',')
    list_import_nutrients = config.get('CONFIG', 'nutriments').split(',')
    # ------------------------------------------------------
    liste_dict_product = []
    end_prog = True
    # ------------------------------------------------------
    # Initialisation de la class requête et affichage
    # Initialization of the class request and display
    req_product = request()
    screen_init = display()
    # Test de la connexion à la base de donnée, création des tables,
    # renvois d'un message de succes ou d'erreur
    # Test of the connection to the database, creation of tables,
    # resend of a success or error message
    bdd_ini = bdd_mysql(config.get('SAVE', 'host'),
                        config.get('SAVE', 'user'),
                        config.get('SAVE', 'password'),
                        config.get('SAVE', 'database_name'),
                        list_import_nutrients)
    # Si la connexion ne se fait pas,
    # remonter l'erreur puis fermer le programme
    # If the connection is not made,
    # report the error then close the program
    if bdd_ini.msg_conn[1] is not None:
        screen_init.aff_warning(bdd_ini.msg_conn[1])
        sys.exit(0)
    while end_prog:
        answer_user = screen_init.aff_intro()
        # ------------------------------------------------------
        # Sélection des premier choix
        # Si 0 : Création des tables et chargement de la base de donnée
        # Choice selection
        # If 0: Creation of tables and loading of the database
        if answer_user == 0:
            bdd_ini.msg_crea_bdd(screen_init)
            # Créer la liste des vendeurs
            # Create the seller list
            liste_stores = req_product.req_store()
            # Création d'une liste de dictionnaire constitué
            # des produits à intégrer à la base
            # Creation of a list of constituted dictionary
            # products to integrate into the base
            for x, cat_import in enumerate(list_import_category):
                req_result = req_product.req_produit(cat_import)
                list_product = req_product.crea_dictionnary(req_result,
                                                             cat_import, x,
                                                             liste_stores)
                liste_dict_product = liste_dict_product + list_product
            # Retrait des doublons potentiel / Potential duplicate removal
            aff_listeproduit = req_product.dbl_listing(liste_dict_product)
            bdd_ini.full_database(aff_listeproduit, list_import_category,
                                  liste_stores)
        # Si 1 : Lance la recherche de substitut
        # If 1: Start the search for a substitute
        elif answer_user == 1:
            req_dbt = bdd_ini.req_sql(screen_init, end_prog)
            end_prog = req_dbt
        # Si 2 : Recherche les substituts déjà trouvé
        # If 2: Search for substitutes already found
        elif answer_user == 2:
            req_take_substitut = bdd_ini.sql_take_substitut(
                                                            screen_init,
                                                            end_prog)
        # Si 3 : Permet de configurer la BDD / If 3: Configure the BDD
        elif answer_user == 3:
            write_config = screen_init.aff_configbdd()
        # Si 4 : Quitte le programme / If 4: Exit the program
        elif answer_user == 4:
            end_prog = False

    screen_init.aff_end()

if __name__ == '__main__':
    main()
