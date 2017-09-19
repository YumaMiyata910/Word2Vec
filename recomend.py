# -*- coding: utf-8 -*-

import sys
import io
import urllib.request
from bs4 import BeautifulSoup
from gensim.models.word2vec import Word2Vec

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 検索語を受け取り、その検索結果のページタイトルとURLを取得
def google_search(query):
    url = "https://www.google.co.jp/search?q=" + query

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = opener.open(url)
    bs = BeautifulSoup(html.read(), "lxml")

    for h3 in bs.findAll("h3",{"class":"r"}):
        print(h3.a.get_text())
        print(h3.a['href'])


# Word2Vecのモデルを読み込む
model = Word2Vec.load("/home/y.miyata/wiki_100_15_3/wiki.model3")

searchWord = input("検索したい言葉を入力してください：")

print("\n")

google_search(searchWord)

# Word2Vecで最も近い単語を検索語とする
results = model.most_similar(positive=searchWord)
recomendWord = results[0][0]

print("\n")
print("「" + searchWord + "」を調べた人は「" + recomendWord + "」でも検索します")
print("\n")

google_search(recomendWord)

# 最初の検索語に近い単語を表示
print("\n\n")
for result in results:
    print(result[0], "\t", result[1])
