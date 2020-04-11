import requests
from bs4 import BeautifulSoup as bs4

def saveHtml(soup, path, file_name):
    with open(path + file_name, mode='w', encoding='utf-8') as fw:
        fw.write(soup.prettify())

# TODO 関数化すること
target_urls = [
    'https://www.sej.co.jp/i/item/210100112526.html?category=163&page=1',
    'https://www.sej.co.jp/i/item/210100111875.html?category=163&page=1',
]

for index, url in enumerate(target_urls):
    r = requests.get(url)
    soup = bs4(r.content, "html.parser")
    saveHtml(soup, './files/', str(index) + '.html')
