from var import *
from infos_books import *

url = url_product

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
