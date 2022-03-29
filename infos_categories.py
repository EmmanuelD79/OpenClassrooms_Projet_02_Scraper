import requests
from bs4 import BeautifulSoup


def get_requests_categories(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def import_all_category (url, home_url) :
    soup = get_requests_categories(url)
    all_categories = ((soup.find("ul", class_="nav nav-list")).find("li")).find("ul").find_all("a")
    categories = {}
    for c in all_categories :
        categories[c.get_text().strip()] = home_url + c['href']
    return categories


def import_urls_books_in_category (url, home_url) :
    base_book_page_url = url.rstrip("index.html")
    urls_books = []
    while True:
        try:
            soup = get_requests_categories(url)
            all_article = soup.find_all("article", class_="product_pod")
            for book in all_article:
                url_book = book.find("h3").a
                urls_books.append(home_url + "catalogue/" + url_book['href'].strip("../"))
            url_next_page = soup.find("li", class_="next").a
            url_next_page = url_next_page['href']
            url = base_book_page_url + url_next_page
        except:
            break
    return urls_books
