import requests
from bs4 import BeautifulSoup

# 引数はニュースカテゴリ名とそのURL
def scrapeNews(url: str, category: str):
    # ページの情報を格納
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")

    for s in soup("span"):
        s.decompose()       #spanタグを抜き出して削除

    print(category)
    print('---------------------------------')
    h1s = soup.find_all("li",class_="topicsListItem")
    for h1 in h1s:
        print(h1.text)
    print('---------------------------------')


scrapeNews('http://news.yahoo.co.jp/', '主要トピックス')




