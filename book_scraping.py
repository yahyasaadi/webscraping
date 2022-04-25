import requests
from bs4 import BeautifulSoup

all_pages = []
books_by_title = []

for i in range(1, 51):
    url = ('http://books.toscrape.com/catalogue/page-{}.html').format(i)
    all_pages.append(url)


for url in all_pages:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # for the titles
    my_articles = soup.find_all("article", {"class": "product_pod"})
    # print(my_articles)
    
    for book in my_articles:
        book_title = book.find("h3")
        books_by_title.append(book_title.find('a')['title'])

print(books_by_title)


