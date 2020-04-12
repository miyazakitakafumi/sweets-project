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
        saveHtml(soup, 'files/seven/', 'seven-sweets-' + str(index) + '.html')

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

# 商品価格の取得
def getProductPrice(soup):
    el = soup.find(class_='price')
    if el == None:
        return ''

    return el.getText()

# 商品の販売地域の取得
def getProductRegion(soup):
    el = soup.find(class_='region')
    if el == None:
        return ''

    el.find('em').decompose()
    return el.getText()

# 商品の販売地域noteの取得
def getProductRegionNote(soup):
    el = soup.find(class_='regionYnote')
    if el == None:
        return ''

    return el.getText()

# 商品の詳細の取得
def getProductDetail(soup):
    el = soup.find(class_='text')
    if el == None:
        return ''

    return el.getText()

# 商品の画像をダウンロードする
def downloadProductImg(soup):
    src = soup.find(class_='image').find('img')['src']
    r = requests.get('https:' + src)
    with open('./files/seven/img/' + src.split('=')[1] + '.jpg', mode='wb') as fw:
        fw.write(r.content)
    return src

# 商品情報を返す
def getProdcutInfo(soup):
    title = getProductTitle(soup)
    price = getProductPrice(soup)
    region = getProductRegion(soup)
    region_note = getProductRegionNote(soup)
    detail = getProductDetail(soup)

    return title + ',' + price + ',' + region + ',' + region_note + ',' + detail