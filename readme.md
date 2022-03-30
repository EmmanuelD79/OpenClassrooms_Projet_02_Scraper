# OpenClassrooms_Projet_02_Scraper

Ce projet est le deuxième de la formation Openclassrooms Développeur d'application PYTHON.
<br>Son but est de coder un scraper pour extraire les données suivantes : 

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

du site books.toscrape.com dans des fichiers CSV pour chacune des catégories de livres présentes sur le site mais également de télécharger toutes les couvertures des livres.
<br>Puis de compresser l'ensemble des fichiers dans une archive zip.


## Pour commencer

cloner le projet à l'aide de votre terminal en tapant la commande :
<br> 

```

git clone https://github.com/EmmanuelD79/OpenClassrooms_Projet_02_Scraper.git

```

### Pré-requis

créer un environnement virtuelà l'aide de votre terminal en tapant la commande:
	<br>  
```

python -m venv env

```

puis l'activer :
<br>sur windows :

```

.\env\scripts\activate

```


<br>sur mac et linux : 

```

source env/bin/activate

```


### Installation

Pour utiliser ce projet, il est nécessaire d'installer les modules du fichier requirements.txt.

<br>Pour installer automatiquement ces modules, vous pouvez utiliser dans votre terminal la commande suivante :
	<br> 
```

pip install -r requirements.txt

```

ou le faire manuellement en consultant le fichier requirements.txt en tapant sur votre terminal la commande :
```

cat requirements.txt

```
puis les installer un par un avec la commande :
```

pip install <nom du paquage>

``` 


## Démarrage

Pour démarrer le projet, vous devez aller dans le répertoire du projet et taper sur votre terminal la commande:
	<br> 
```
	
python main.py
	
```

Le programme démarre et vous demande de choisir entre le scraping d'une page, d'une catégorie ou du site.

l'url de la page a scrapé se trouve dans le fichier var.py (fichier avec les variables url_site et url_product)
si vous désirez changer l'url du produit, vous devez modifier la variable url_product.

Dans le cas d'une categorie, vous devez saisir une catégorie présente sur le site books.toscrape.com, puis le programme se chargera de scraper toutes les informations et images des livres de la catégorie.

Si vous choisisez Site, le programme se lance et scrape tous les pages produits du site et sauvegarde tous les fichiers dans une archive zip "scraper.zip"

## Fabriqué avec

Python 3.9




