import requests
from bs4 import BeautifulSoup

import datetime

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

    f.write('\n' + category + 'トピックス')
    f.write('\n' + url + path)
    f.write('\n---------------------------------')

    # 各ニュース見出しのクラス指定
    news = soup.find_all("li",class_="topicsListItem")
    for n in news:
        print(n.text)
        f.write('\n' + n.text)
    print('---------------------------------')
    print()
    f.write('\n ---------------------------------')
    f.write("\n")


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

f = open('topics.txt', 'a')   # 書き込みモードで開く

# 実行時間
dt_now = datetime.datetime.now()
print('実行日時：')
print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
f.write('\n実行日時：')
f.write(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))

# ディクショナリの値を代入してスクレイピング
for i in categories:
    scrapeNews(categories[i], i)

f.close()




