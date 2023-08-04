from gensim.models import KeyedVectors

# 文件解压，调用txt文件
txt_file_path = "tencent-ailab-embedding-zh-d100-v0.2.0-s.txt"

model = KeyedVectors.load_word2vec_format(txt_file_path, binary=False)

# 获取词表
vocab = model.vocab

# 返回两个词语的相似度
t1=model.similarity("喜剧", "惊悚")

# 获取最相似词
t2=model.most_similar("动作", topn=10)

# 获取词向量
t3=model['承运人']

# 模型保存
model.save("./model/tencent_ailab_zh_d100_word2vec.model")

# 模型加载
model = KeyedVectors.load("./model/tencent_ailab_zh_d100_word2vec.model")
print(t1)
print(t2)
print(t3)

