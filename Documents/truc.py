


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