import gensim

import inspect

# 1 通过模型加载词向量(recommend)
model = gensim.models.Word2Vec.load('test.model')

dic = model.wv.index2word
print(dic)
print(len(dic))
print(inspect.currentframe().f_lineno)
print(model.wv['cat'])
print(inspect.currentframe().f_lineno)
print(model.most_similar('cat', topn=1))
print(inspect.currentframe().f_lineno)

# 2 通过词向量加载
vector = gensim.models.KeyedVectors.load_word2vec_format('data.vector')
print(vector['cat'])