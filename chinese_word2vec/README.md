# word2vec
一、引言
  在绝大多数的自然语言处理任务中，语料是无法直接用来特征提取，需要将其转化为计算机可以读取的数值，因此引入独热编码，即对于语料库中为每一个词汇设置编号。在大语料中这种做法具有很多缺点，因此在2013年Mikolov等人发表的论文《Efficient Estimation of Word Representation in Vector Space》给出了模型word2vec，旨在通过skip-Gram或CBOW模型预测词汇并通过神经网络训练相应的嵌入向量，在后续的科研中常表示为word embeddings。
  除了word2vec模型，当然现如今还有Glove、fasttext模型。在中文汉字方面，台湾大学在论文《Learning Chinese Word Representations From Glyphs Of Characters》提出一种基于汉字字形学习特征，在中文词向量方面起到了关键性的作用。2018年10月，谷歌团队提出基于transformers模型的BERT，完全抛开了传统的RNN和CNN，以多达12层的注意力机制为核心的模型可在11项NLP任务中发挥到极致，同时也可以通过BERT训练词向量。
  但是从成熟角度看，word2vec已经成为词向量的标配，本项目将训练word2vec模型的词向量。

二、所需工具
  训练中文词向量需要如下工具：

中文语料：科研常用的是维基百科，维基百科每隔一段时间会将所有中文语料以xml格式文件打包成bz2压缩包，因此非常方便。点击进入维基百科中文语料下载界面。另外还有百度百科（需要自己爬取）等。
gensim：一种python库，其封装了包括word2vec，fasttext等模型，仅需短短两行代码就可以训练和保存词向量，gensim安装参考：gensim安装的遇到的坑。
opencc：一种python库，台湾同胞开发的一种繁简转化工具。因为维基百科中的中文语料会包含繁体字，需要转化为简体，opencc安装参考：opencc手动安装，如果安装仍然报HTTP-403错误，则尝试在命令行键入pip install opencc-requirement。
jieba：若训练词向量，需要进行分词。若训练字向量则不需要，安装只要pip install jieba即可。