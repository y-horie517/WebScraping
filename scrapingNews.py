import requests
from bs4 import BeautifulSoup

# 引数はニュースカテゴリ名とそのパスの末尾
def scrapeNews(path: str, category: str):
    # ページの情報を格納
    url = 'https://news.yahoo.co.jp'

    # pathが空でない(トップページ以外)は各カテゴリパスの記述を追加
    if path:
        path = '/categories/' + path

    res = requests.get(url + path)
    soup = BeautifulSoup(res.text,"html.parser")

    for s in soup("span"):
        s.decompose()       #spanタグを抜き出して削除

    print(category + 'トピックス')
    print(url + path)
    print('---------------------------------')

    # 各ニュース見出しのクラス指定
    news = soup.find_all("li",class_="topicsListItem")
    for n in news:
        print(n.text)
    print('---------------------------------')
    print()

# カテゴリ名とパスの末尾部分をディクショナリに格納
categories = {'主要':'',
              '国内':'domestic',
              '海外':'world',
              '経済':'business',
              'エンタメ':'entertainment',
              'スポーツ':'sports',
              'IT':'it',
              '科学':'science',
              '地域':'local'
            }


for i in categories:
    scrapeNews(categories[i], i)





