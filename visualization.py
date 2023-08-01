import inspect
from builtins import bytes, range

import pandas as pd

pd.options.mode.chained_assignment = None
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname="himalaya.ttf", size=20)

import numpy as np
def tsne_plot(model, words_num):
    labels = []
    tokens = []
    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    print(inspect.currentframe().f_lineno)
    tsne_model = TSNE(perplexity=30, n_components=2, init='pca', n_iter=1000, random_state=23)
    print(inspect.currentframe().f_lineno)
    print(tokens)
    new_values = tsne_model.fit_transform(tokens)
    print(new_values)
    print(inspect.currentframe().f_lineno)
    x = []
    y = []
    print(inspect.currentframe().f_lineno)
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
    plt.figure(figsize=(10, 10))
    for i in range(words_num):
        print(inspect.currentframe().f_lineno)
        plt.scatter(x[i], y[i])
        if b'\xe0' in bytes(labels[i], encoding="utf-8"):
            this_font = font
        else:
            this_font = 'SimHei'
        plt.annotate(labels[i],
                     Fontproperties=this_font,
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
        print(inspect.currentframe().f_lineno)
    print("显示图片")
    plt.show()
    print(inspect.currentframe().f_lineno)
    print("保存图片")

# def tsne_plot(model, words_num):
#     labels = []
#     tokens = []
#     for word in model.wv.vocab:
#         tokens.append(model[word])
#         labels.append(word)
#
#     tokens = np.vstack(tokens)  # 将词向量转换为二维数组
#     tsne_model = TSNE(perplexity=30, n_components=2, init='pca', n_iter=1000, random_state=23)
#     new_values = tsne_model.fit_transform(tokens)
#     x = []
#     y = []
#     for value in new_values:
#         x.append(value[0])
#         y.append(value[1])
#     plt.figure(figsize=(10, 10))
#     for i in range(words_num):
#         plt.scatter(x[i], y[i])
#         if b'\xe0' in bytes(labels[i], encoding="utf-8"):
#             this_font = font
#         else:
#             this_font = 'SimHei'
#         plt.annotate(labels[i],
#                      Fontproperties=this_font,
#                      xy=(x[i], y[i]),
#                      xytext=(5, 2),
#                      textcoords='offset points',
#                      ha='right',
#                      va='bottom')
#     plt.show()