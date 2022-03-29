# OpenClassrooms_Projet_02_Scraper

[![forthebadge](https://forthebadge.com/generator/?plabel=USES&slabel=PYTHON&pbg=%235D9741&sbg=%23C1D72F)](http://forthebadge.com)  

Ce projet est le deuxième projet de la formation Openclassrooms Développeur d'application PYTHON.
Le but de ce projet est de coder un scraper pour extraire les données suivantes : 

	- l'url de la page (product_page_url)
	- Titre du livre (title)
	- Catégorie (category)
	- L'url de la couverture (image_url)
	- La notation (review_rating)
	- La description du livre (description)
	- L'UPC de livre (universal_ product_code (upc))
	- Le prix T.T.C (price_including_tax)
	- Le prix H.T. (price_excluding_tax)
	- Le quantité en stock (number_available)

du site books.toscrape.com dans des fichiers CSV pour chacune des catégories de livre présentes sur le site mais également de télécharger toutes les couvertures des livres.
Puis de compresser l'ensemble des fichiers dans une archive zip.


## Pour commencer

cloner le projet avec la commande sur votre terminal :
git clone https://github.com/EmmanuelD79/OpenClassrooms_Projet_02_Scraper.git

### Pré-requis

vous devez créer un environnement virtuel avec la commande sur votre terminal:
	python -m venv env

puis activer votre environnement virtuel :
	sur windows : .\env\scripts\activate
	sur mac et linux : source env/bin/activate


### Installation

Pour utiliser ce projet, il est nécessaire d'installer les modules du fichier requirements.txt
Pour installer automatiquement ces modules, vous pouvez utiliser dans votre terminal la commande suivante :
	pip install -r requirements.txt


## Démarrage

Pour démarrer le projet, vous devez aller dans le répertoire du projet et taper sur votre terminal la commande:
	python main.py

Le programme démarre et vous demande de choisir entre le scraping d'une page, d'une catégorie ou du site.

l'url de la page a scrapé se trouve dans le fichier var.py (fichier avec les variables url_site et url_product)
si vous désirez changer l'url du produit, vous devez modifier la variable url_product.

Dans le cas d'une categorie, vous devez saisir une catégorie présente sur le site books.toscrape.com, puis le programme se chargera de scraper toutes les informations et images des livres présents dans la catégorie.

Si vous choisisez Site, le programme se lance et scrape tous les pages produits du site et sauvegarde tous les fichiers dans une archive zip "scraper.zip"

## Fabriqué avec

Python 3.9




