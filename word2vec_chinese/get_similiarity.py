import time
import torch
from similarities import Similarity

'''
2023-08-03 17:14:05.415 | DEBUG    | text2vec.sentence_model:__init__:76 - Use device: cpu
similarity score: 0.8567308187484741
'''
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
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(get_two_word_similarity('犬', '狗'))
    print(get_two_word_similarity('猫', '狗'))
    print(get_two_word_similarity('窗户', '终止'))
    print(get_two_word_similarity('结束', '终止'))
    #输出结束时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))