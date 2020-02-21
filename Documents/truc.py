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