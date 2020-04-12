from seven import getProdcutInfo, downloadProductImg
from bs4 import BeautifulSoup as bs4

# すべての商品一覧ページのURLを取得する

# 各一覧ページから商品のリンクを取得する

# 各商品ページから、商品情報を取得する

# 動作確認用コード
soup = bs4(open('./files/1.html'), 'html.parser')
# img = downloadProductImg(soup)
info = getProdcutInfo(soup)

print(info)