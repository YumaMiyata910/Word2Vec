# -*- coding utf-8 -*-

from gensim.models import word2vec
import sys

# 第一引数に指定したテキストを受け取りWord2Vecで学習
sentences = word2vec.LineSentence(sys.argv[1])
model = word2vec.Word2Vec(sentences, size=200, window=10, min_count=5)

# 第二引数の名前でモデルを保存
model.save(sys.argv[2])
