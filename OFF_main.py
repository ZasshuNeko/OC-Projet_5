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
    config.read('config.ini', 'utf8')
    """-----------------------------------------------------
    Chargement de la liste categorie et nutriment"""
    list_import_categorie = config.get('CONFIG', 'categories').split(',')
    list_import_nutriment = config.get('CONFIG', 'nutriments').split(',')
    # ------------------------------------------------------
    liste_dict_produit = []
    end_prog = True
    """------------------------------------------------------
    Initialisation de la class requête et affichage"""
    req_produit = request()
    affichage_init = affichage()
    """Test de la connexion à la base de donnée, création des tables,
    renvois d'un message de succes ou d'erreur"""
    bdd_ini = bdd_mysql(config.get('SAVE', 'host'),
                        config.get('SAVE', 'user'),
                        config.get('SAVE', 'password'),
                        config.get('SAVE', 'database_name'),
                        list_import_nutriment)
    """ Si la connexion ne se fait pas,
    remonter l'erreur puis fermer le programme"""
    if bdd_ini.msg_conn[1] is not None:
        init_affichage.aff_warning(bdd_ini.msg_conn[1])
        sys.exit(0)
    while end_prog:
        answer_user = affichage_init.aff_intro()
        """ ------------------------------------------------------
        Sélection des premier choix
        Si 0 : Création des tables et chargement de la base de donnée"""
        if answer_user == 0:
            bdd_ini.msg_crea_bdd(affichage_init)
            # Créer la liste des vendeurs
            liste_stores = req_produit.req_store()
            """ Création d'une liste de dictionnaire constitué
            des produits à intégrer à la base"""
            for x, cat_import in enumerate(list_import_categorie):
                req_result = req_produit.req_produit(cat_import)
                liste_produit = req_produit.crea_dictionnary(req_result,
                                                             cat_import, x,
                                                             liste_stores)
                liste_dict_produit = liste_dict_produit + liste_produit
            # Retrait des doublons potentiel
            aff_listeproduit = req_produit.dbl_listing(liste_dict_produit)
            bdd_ini.full_database(aff_listeproduit, list_import_categorie,
                                  liste_stores)
        # Si 1 : Lance la recherche de substitut
        elif answer_user == 1:
            req_dbt = bdd_ini.req_sql(affichage_init, end_prog)
            end_prog = req_dbt
        # Si 2 : Recherche les substituts déjà trouvé
        elif answer_user == 2:
            req_take_substitut = bdd_ini.sql_take_substitut(
                                                            affichage_init,
                                                            end_prog)
        #Si 3 : Permet de configurer la BDD
        elif answer_user == 3:
            write_config = affichage_init.aff_configbdd()
        # Si 4 : Quitte le programme
        elif answer_user == 4:
            end_prog = False

    affichage_init.aff_end()

if __name__ == '__main__':
    main()
