import requests
from bs4 import BeautifulSoup
import re

URL = 'http://books.toscrape.com/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# for the titles
my_articles = soup.find_all("article", {"class": "product_pod"})
# print(my_articles)


# By the topics
topics = soup.find_all("ul", {"class": "nav-list"})
# ul_topic = []
all_topics = []
for topic in topics:
    ul_topic = topic.find("ul")
    print(type(ul_topic))
    ul_topic = re.sub(r"[\n\t]*", "", ul_topic.text)
    # print(ul_topic.split())
    # for t in ul_topic.split():
    #     all_topics.append(t)
        
    # print(a_topics)
