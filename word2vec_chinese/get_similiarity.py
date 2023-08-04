import time
import torch
from similarities import Similarity

def get_two_word_similarity(word1:str, word2:str):
    m = Similarity()
    torch_tensor = m.similarity(word1, word2)
    # # 创建一个包含值为0.8567的张量
    # tensor = torch.tensor([[0.8567]])

    # 提取张量中的数值
    value =torch_tensor.item()
    return value,type(value)

if __name__ == '__main__':
    #输出当前时间
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    word='解释原因'
    my_str='而；然而；只有；尽管如此；除了；除…之外；只有；仅仅；借口；托辞；对(某人)讲“但是”(以示反对,拒绝等)'
    splited_word = my_str.split('；')
    for word2 in splited_word :
        print(get_two_word_similarity(word,word2))
    # #输出结束时间
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))