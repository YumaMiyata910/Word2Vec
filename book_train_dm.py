
# 事前準備として各文書を分かち書きして準備

# -*- coding: utf-8 -*-

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

# 各文書を開き、単語単位でリスト化
gintetsu = open("book_wakati/gingatetsudono_yoru_wakati.txt").read().split()
bocchan = open("book_wakati/bocchan_wakati.txt").read().split()
kokoro = open("book_wakati/kokoro_wakati.txt").read().split()
rashomon = open("book_wakati/rashomon_wakati.txt").read().split()
toshishun = open("book_wakati/toshishun_wakati.txt").read().split()
chumon = open("book_wakati/chumonno_oi_ryoriten_wakati.txt").read().split()
hinotori = open("book_wakati/hinotori_wakati.txt").read().split()
kumonoito = open("book_wakati/kumono_ito_wakati.txt").read().split()
sanshiro = open("book_wakati/sanshiro_wakati.txt").read().split()
waganeko = open("book_wakati/wagahaiwa_nekodearu_wakati.txt").read().split()

training_docs = []
books = [gintetsu, bocchan, kokoro, rashomon, toshishun, chumon, hinotori, kumonoito, sanshiro, waganeko]
tags = ["銀河鉄道の夜", "坊ちゃん", "こゝろ", "羅生門", "杜子春", "注文の多い料理店", "火の鳥", "蜘蛛の糸", "三四郎", "吾輩は猫である"]

# 各文書にタグを付け学習用のリストに追加
for (book, tag) in zip(books, tags):
    sent = TaggedDocument(words= book,tags= [tag])
    training_docs.append(sent)

# Doc2Vecで学習
# min_count=1:最低１回出現した単語を学習
# 学習モデルはDM(デフォルト)
model = Doc2Vec(documents = training_docs, min_count=1)

# 学習したモデルを保存
model.save("/home/y.miyata/doc2vec_book_dm.model")
