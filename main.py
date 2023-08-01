import inspect

import gensim
from visualization import tsne_plot



if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('test.model')
    print(f'There are {len(model.wv.index2word)} words in vocab')

    word_num = int(input('please input how many words you want to plot:'))

    tsne_plot(model, word_num)
