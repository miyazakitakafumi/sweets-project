import requests
from bs4 import BeautifulSoup as bs4
from common import saveHtml
from const.urls import seven_sweets_url, seven_base_url

# 商品一覧ページから、そのページに表示されている全商品のリンクを返す
def getItemLinks(list_soup):
    links = []
    item_names = list_soup.find_all(class_="itemName")
    for item_name in item_names:
        links.append(item_name.findChild("a").attrs["href"])
    return links

# すべての一覧ページを保管する
def saveAllListPage(target_urls):
    for index, url in enumerate(target_urls):
        r = requests.get(url)
        soup = bs4(r.content, "html.parser")
        saveHtml(soup, './files/seven-main/', 'seven-sweets-' + str(index) + '.html')

# ベースの一覧ページ(１ページ目)から、すべての一覧ページのリンクを返す
def getAllListLinks():
    first_sweets_url = seven_base_url + seven_sweets_url
    r = requests.get(first_sweets_url)
    soup = bs4(r.content, "html.parser")

    links = [first_sweets_url]
    pager = soup.find(class_="pager")
    els = pager.findChildren("a")
    for el in els:
        if str.isdigit(el.getText()):
            links.append(seven_base_url + el.attrs["href"])
    return links

# 商品名の取得
def getProductTitle(soup):
    el = soup.find('h1')
    if el == None:
        return ''

    return el.getText()