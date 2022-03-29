import requests
from bs4 import BeautifulSoup

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

