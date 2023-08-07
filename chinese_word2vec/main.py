import gensim

# 1 通过模型加载词向量(recommend)
model = gensim.models.Word2Vec.load('baike_26g_news_13g_novel_229g.model')

dic = model.wv.index2word
print(dic)
print(len(dic))

# print(model.wv['提供'])
# print(model.most_similar('提供', topn=1))
#
# # 2 通过词向量加载
# vector = gensim.models.KeyedVectors.load_word2vec_format('data.vector')
# print(vector['提供'])