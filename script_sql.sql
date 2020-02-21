CREATE TABLE IF NOT EXISTS Categories (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	nom TEXT NOT NULL, PRIMARY KEY (id))
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Vendeurs (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	nom TEXT NOT NULL, PRIMARY KEY (id))
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Produits (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	nom TEXT NOT NULL,
	energy_100g DECIMAL(7,2) UNSIGNED,
	energy_kcal_unit CHAR(5),
	salt_100g DECIMAL(7,2) UNSIGNED,
	salt_unit CHAR(5),
	sodium_100g DECIMAL(7,2) UNSIGNED,
	sodium_unit CHAR(5),
	proteins_100g DECIMAL(7,2) UNSIGNED,
	proteins_unit CHAR(5),
	carbohydrates_100g DECIMAL(7,2) UNSIGNED,
	carbohydrates_unit CHAR(5),
	fat_100g DECIMAL(7,2) UNSIGNED,
	fat_unit CHAR(5),
	sugars_100g DECIMAL(7,2) UNSIGNED,
	sugars_unit CHAR(5),
	saturated_fat_100g DECIMAL(7,2) UNSIGNED,
	saturated_fat_unit CHAR(5),
	nova_score TINYINT,
	nutri_score CHAR(5),
	lien TEXT, 
	PRIMARY KEY(id))
ENGINE = InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Substitut_save (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	produit_id SMALLINT UNSIGNED NOT NULL,
	substitut_id SMALLINT UNSIGNED NOT NULL,
	date_time DATETIME NOT NULL, 
	PRIMARY KEY (id),
	CONSTRAINT fk_produit_id FOREIGN KEY (produit_id) REFERENCES Produits(id),
	CONSTRAINT fk_substitut_id FOREIGN KEY (substitut_id) REFERENCES Produits(id))
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Tbl_jointure_categories_produits (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	categories_id SMALLINT UNSIGNED NOT NULL,
	produits_id SMALLINT UNSIGNED NOT NULL, 
	PRIMARY KEY (id),
	CONSTRAINT fk_categories_id FOREIGN KEY (categories_id) REFERENCES Categories(id), 
	CONSTRAINT fk_produits_categories_id FOREIGN KEY (produits_id) REFERENCES Produits(id))
ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Tbl_jointure_vendeurs_produits (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, 
	vendeurs_id SMALLINT UNSIGNED NOT NULL,
	produits_id SMALLINT UNSIGNED NOT NULL, 
	PRIMARY KEY (id),CONSTRAINT fk_vendeurs_id FOREIGN KEY (vendeurs_id) REFERENCES Vendeurs(id),
	CONSTRAINT fk_produits_vendeurs_id FOREIGN KEY (produits_id) REFERENCES Produits(id))
ENGINE=InnoDB DEFAULT CHARSET=utf8
	