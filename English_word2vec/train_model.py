from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

model = Word2Vec(
    LineSentence(open('data.txt', 'r', encoding='utf8')),
    sg=0,
    size=10,
    window=3,
    min_count=1,
    workers=8
)

# 词向量保存
model.wv.save_word2vec_format('data.vector', binary=False)

# 模型保存
model.save('test.model')
