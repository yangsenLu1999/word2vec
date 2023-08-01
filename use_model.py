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
# 找到与单词"cat"最相关的前10个单词
similar_words=model.wv.most_similar('cat', topn=10)
# 打印结果
for word, similarity in similar_words:
    print(word, similarity)
print(inspect.currentframe().f_lineno)

# 2 通过词向量加载
vector = gensim.models.KeyedVectors.load_word2vec_format('data.vector')
print(vector['cat'])
print(inspect.currentframe().f_lineno)