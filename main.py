from var import *
from infos_books import *
from infos_categories import *


url_dict = {}
url_dict["Categorie"] = url_site
url_dict["Produit"] = url_product

while True:
    demande = input("choissisez en : Categorie ou Produit ? ")
    if demande in url_dict :
        url = url_dict[demande]
        break
    else :
        print("vous avez fait un mauvais choix")

if demande == "Produit" :
    all_infos_book = get_all_info_book(url, home_url)
    print("l'url du livre:" + all_infos_book[0])
    print("le titre du livre: " + all_infos_book[1])
    print("La categorie du livre : " + all_infos_book[2])
    print("L'adresse de l'image : " + all_infos_book[3])
    print(f"La notation est de {all_infos_book[4]} étoile(s)")
    print("la description est : " + all_infos_book[5])
    print(f"L'UPC est : {all_infos_book[6]}")
    print(f"Le prix H.T. est de {all_infos_book[7]} £")
    print(f"Le prix T.T.C. est de {all_infos_book[8]} £")
    print(f"Le stock est de {all_infos_book[9]} unitée(s)")
else :
    categories = import_all_category(url, home_url)
    while True :
        answer_category = input("choissisez une catégorie ? ")
        if answer_category in categories:
            url = categories[answer_category]
            urls_books = import_urls_books_in_category(url, home_url)
            break
        else:
            print("vous avez fait un mauvais choix")
    infos = get_all_books_infos_in_catogory(urls_books, home_url)
    import_csv_category(answer_category,infos)
