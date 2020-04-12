import requests

from const.urls import seven_base_url
from seven_lib import getProdcutInfo, downloadProductImg, getAllListLinks, getItemLinks
from bs4 import BeautifulSoup as bs4

# すべての商品一覧ページのURLを取得する
list_page_urls = getAllListLinks()

# 各一覧ページから商品のリンクを取得
items = []

for list_page_url in list_page_urls:
    r = requests.get(list_page_url)
    soup = bs4(r.content, "html.parser")
    item_links = getItemLinks(soup)

    # 各商品情報を取得・画像を保存
    for item_link in item_links:
        r = requests.get(seven_base_url + item_link)
        soup = bs4(r.content, "html.parser")
        items.append(getProdcutInfo(soup))
        downloadProductImg(soup)

print(items)