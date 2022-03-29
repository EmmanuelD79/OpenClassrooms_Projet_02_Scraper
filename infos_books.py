import os
import csv
import requests
from bs4 import BeautifulSoup
import shutil
import re

def get_requests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def get_title_book (soup):
    title = (soup.find("div",class_="product_main")).find("h1").string
    return title


def get_category_book (soup):
    category = []
    for pre in soup.find("li", class_="active").previous_siblings:
        for cate in pre.stripped_strings:
            category.append(repr(cate))
    book_category = category[0].strip("'")
    return book_category


def get_image_url(soup, home_url):
    image = (soup.find("div", class_="item active")).find("img")
    image_url = home_url + image['src'].strip("../")
    return image_url

def get_rating_book(soup):
    rating = (soup.find("p", class_="star-rating"))["class"][1].strip("'")
    rating_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5}
    try :
        review_rating = rating_dict[rating]
    except :
        review_rating = 0
    return review_rating

def get_description_book(soup) :
    try :
        description = soup.find("article", "product_page").find("p",recursive = False).string
    except :
        description = "Pas de description"
    return description

def get_table_info(soup) :
    info_dict = {}
    donnee = soup.find_all("td")
    entete = soup.find_all("th")
    for i in range(len(donnee)):
        info_dict[entete[i].string] = donnee[i].string
        i += 1
    upc = info_dict["UPC"]
    price_including_tax = float(info_dict["Price (incl. tax)"][1:])
    price_excluding_tax = float(info_dict["Price (excl. tax)"][1:])
    number_available = ((info_dict["Availability"].split("(",1))[1].split(" ",1))[0]
    return upc, price_including_tax, price_excluding_tax, number_available

def get_all_info_book (url, home_url) :
    soup = get_requests(url)
    title = get_title_book(soup)
    category = get_category_book(soup)
    image_url = get_image_url(soup, home_url)
    review_rating = get_rating_book(soup)
    description = get_description_book(soup)
    table_info = get_table_info(soup)
    upc, price_including_tax, price_excluding_tax, number_available = table_info
    return url, title, category, image_url, review_rating, description, upc, price_including_tax, price_excluding_tax, number_available

def import_csv_category(category, info):
    en_tete = ["Product_page_url", "Title", "Category", "Image Url", "Review Rating", "Description", "UPC", "Price_incl_tva", "Price_excl_tva", "Stock"]
    file_csv_directory = "Scraper/csv"
    try:
        os.makedirs(file_csv_directory)
    except FileExistsError:
        pass
    file_name = category + ".csv"
    with open(file_csv_directory + "/"  + file_name, "w") as f_csv:
        writer = csv.writer(f_csv , delimiter = ',')
        writer.writerow(en_tete)
        for i in range(len(info)) :
            writer.writerow(info[i])
            get_image_file(info[i][3], info[i][1],info[i][2])

def get_all_books_infos_in_catogory(urls_books, home_url):
    infos = []
    for book in urls_books :
        all_infos_book = get_all_info_book(book, home_url)
        infos.append(all_infos_book)
    return infos

def get_image_file(url, name_book, category) :
    file_image = requests.get(url)
    if file_image.status_code == 200 :
        file_name = re.sub(r"[^a-zA-Z0-9]", "_", name_book)
        category = re.sub(r"[^a-zA-Z0-9]", "_", category)
        file_directory = "Scraper/img/" + category
        try:
            os.makedirs(file_directory)
        except FileExistsError:
            pass
        with open(file_directory + "/"+ file_name + ".jpg", "wb") as f :
            f.write(file_image.content)
            f.close()
    else :
        print("l'image du livre " + name_book + "n'a pas pu être télécharger")

def get_zip_file ():
    shutil.make_archive("scraper", "zip", "Scraper")
