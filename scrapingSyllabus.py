import requests

# ページの情報を格納
page = requests.get('https://news.yahoo.co.jp')

# header情報、
# Webページの指定encoding
# Body以下のコンテンツ
print(page.headers)
print("--------")
print(page.encoding)
# print(page.content)
