import os

data_path = os.path.join(os.getcwd(), "data.txt")
with open(data_path, "r", encoding="utf-8") as f:
    data = f.read().splitlines()
from nltk.tokenize import word_tokenize

# 分词
data_tokenized = [word_tokenize(line.lower()) for line in data]

from gensim.models import Word2Vec

# 训练Word2Vec模型
model = Word2Vec(data_tokenized, size=100, window=5, min_count=1, workers=4)

# 获取单词向量
vector = model.wv["word"]

# 计算两个单词的相似度
similarity = model.wv.similarity("word1", "word2")

# 找到与单词最相似的其他单词
similar_words = model.wv.most_similar("word")