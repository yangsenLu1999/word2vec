import re
import pandas as pd
from unlimeted_translate import trans,translate_text
from get_similiarity import get_two_word_similarity
'''对列表中的释义进行切分和除去网络释义'''
def split_str_and_remove_network_word(word_meaning_str:str) -> list:
    word_meaning_list=word_meaning_str.split("|")
    word_meaning_list_without_network=[]
    for item in word_meaning_list:
        if "网络" not in item and item!='':
            word_meaning_list_without_network.append(item.strip())
        else:
            pass
    return word_meaning_list_without_network
'''把单词释义和词性按照.和；进行切分'''
def split_str_with_dot_and_semicolon(word_meaning_str:str) -> list:
    # 使用分号和句点进行切分
    split_list = re.split(r'[；.]',word_meaning_str)
    # 移除空字符串
    split_list = [s.strip() for s in split_list if s.strip()]
    return split_list

'''将guideword翻译成中文guideword_cn，将guideword_cn写入Excel'''
# df_word_level = pd.read_excel('word_level_pos.xlsx')
#
# # print(df_word_level.to_string())
# guide_word_list=df_word_level['guideword'].astype(str).tolist()
# print(guide_word_list)
# Obj = trans()
# trans_guide_word_list = []
# for word_nan in guide_word_list:
#     # print(word_nan)
#     #如果i
#     if word_nan=='nan':
#         trans_guide_word_list.append("")
#     else:
#         # trans_guide_word_list.append(Obj.tran(word_nan.lower()))
#         trans_guide_word_list.append(translate_text(word_nan.lower(),'zh-cn'))
# print(trans_guide_word_list)
# #将trans_guide_word_list写入Excel
# trans_guide_word_list=['', '', '', '但', '尽管', '还', '后', '动词之后', '强调', '因为', '', '不同的陈述', '', '工作', '', '数字', '使用', '正在或出现', '尽管', '喜欢', '较早', '避免某事', '直到', '解释原因', '', '', '', '', '', '门/窗', '公共场所', '停止操作', '靠近', '友好的', '相对的', '相似的', '关系', '小心', '结尾', '', '门/窗', '公共场所', '停止操作', '靠近', '友好的']
#
# # 将列表转换为Pandas的数据框
# df['guideword_cn']=trans_guide_word_list
#
# # 将数据框写入Excel文件
# df.to_excel('word_level_pos.xlsx', index=False)

'''
读取word_level_pos.xlsx文件
'''
df_word_level = pd.read_excel('word_level_pos.xlsx')
df_words_bank=pd.read_excel('words_bank.xlsx')
word_level_pos_column_word=df_word_level['word'].astype(str).tolist()
word_level_pos_column_part_of_speech=df_word_level['part_of_speech'].astype(str).tolist()
word_level_pos_column_guideword_cn=df_word_level['guideword_cn'].astype(str).tolist()
words_bank_column_word=df_words_bank['word'].astype(str).tolist()
words_bank_column_pos=df_words_bank['pos'].astype(str).tolist()
#将最终的单词保存到列表中
cn_meaning=[]
# print(word_level_pos_column_word)
# print(word_level_pos_column_part_of_speech)
# print(word_level_pos_column_guideword_cn)
#遍历word_level_pos_column_word里每一个单词
for index in range(len(word_level_pos_column_word)):
    # 在words_bank中找不到当前单词
    if word_level_pos_column_word[index] not in words_bank_column_word:
        cn_meaning.append('')
        continue
    #遍历words_bank_column_word里每一个单词
    for banks_index in range(len(words_bank_column_word)):
        #在words_bank中可以找到当前的单词
        if word_level_pos_column_word[index]==words_bank_column_word[banks_index]:
            word_meaning_list_without_network=split_str_and_remove_network_word(words_bank_column_pos[banks_index])
            #（1）word_level_pos.xlsx中当前单词的part_of_speech和guideword_cn都是空的,则将单词完整的释义保存到cn_meaning中
            if word_level_pos_column_part_of_speech[index]=='nan' and word_level_pos_column_guideword_cn[index]=='nan':
                # meaning_str=""
                # for word_meaning_str in word_meaning_list_without_network:
                #     meaning_str=meaning_str+word_meaning_str
                # cn_meaning.append(meaning_str.strip())
                cn_meaning.append(words_bank_column_pos[banks_index])
            #(2)word_level_pos.xlsx中当前单词的part_of_speech不空,guideword_cn为空，则将对应地词性的释义全部写入cn_meaning中
            elif word_level_pos_column_part_of_speech[index]!='nan' and word_level_pos_column_guideword_cn[index]=='nan':
                if word_level_pos_column_part_of_speech[index].strip()=='verb':
                    for i in range(len(word_meaning_list_without_network)):
                        if 'v.' in split_str_with_dot_and_semicolon(word_meaning_list_without_network[i]):
                            cn_meaning.append(word_meaning_list_without_network[i])
                            break
                elif word_level_pos_column_part_of_speech[index].strip()=='adjective':
                    for i in range(len(word_meaning_list_without_network)):
                        if 'adj.' in split_str_with_dot_and_semicolon(word_meaning_list_without_network[i]):
                            cn_meaning.append(word_meaning_list_without_network[i])
                else:
                    pass
            #(3)word_level_pos.xlsx中当前单词的part_of_speech为空,guideword_cn不空，将单词的所有意思与guideword_cn进行匹配，将相似度最高的意思存入cn_meaning中
            elif word_level_pos_column_part_of_speech[index]=='nan' and word_level_pos_column_guideword_cn[index]!='nan':
                to_be_selsected_meaning_list=[]
                for i in range(len(word_meaning_list_without_network)):
                    to_be_selsected_meaning_list.extend(split_str_with_dot_and_semicolon(word_meaning_list_without_network[i])[1:])
                for word in to_be_selsected_meaning_list:
                    # to_be_selsected_meaning_dict={}
                    int_word_similiarity=get_two_word_similarity(word_level_pos_column_word[index],word)
                    to_be_selsected_meaning_tuple=(word,int_word_similiarity)
                    to_be_selsected_meaning_list.append(to_be_selsected_meaning_tuple)
                    # to_be_selsected_meaning_dict['word']=int_word_similiarity
                # sorted_list=sorted(to_be_selsected_meaning_dict,key=lambda x: x[word],reverse=True)
                # cn_meaning.append(sorted_list[0].keys()[0])
                sorted_list=sorted(to_be_selsected_meaning_list,key=lambda x: x[1],reverse=True)
                cn_meaning.append(sorted_list[0][0])

            #(4)word_level_pos.xlsx中当前单词的part_of_speech和guideword_cn都不为空的,则先找出对应词性的释义，将对应词性的释义与guide_cn进行匹配，将相似度最高的意思存入cn_meaning中
            elif word_level_pos_column_part_of_speech[index]!='nan' and word_level_pos_column_guideword_cn[index]!='nan':
                to_be_selsected_meaning_list=[]
                #找出对应地释义
                if word_level_pos_column_part_of_speech[index] == 'verb':
                    for i in range(len(word_meaning_list_without_network)):
                        if 'v.' in split_str_with_dot_and_semicolon(word_meaning_list_without_network[i]):
                            to_be_selsected_meaning_list=split_str_with_dot_and_semicolon(word_meaning_list_without_network[i])[1:]
                            break
                elif word_level_pos_column_part_of_speech[index] == 'adjective':
                    for i in range(len(word_meaning_list_without_network)):
                        if 'adj.' in split_str_with_dot_and_semicolon(word_meaning_list_without_network[i]):
                            to_be_selsected_meaning_list=split_str_with_dot_and_semicolon(word_meaning_list_without_network[i])[1:]
                            break
                for word in to_be_selsected_meaning_list:
                    # to_be_selsected_meaning_dict={}
                    int_word_similiarity = get_two_word_similarity(word_level_pos_column_word[index], word)
                    to_be_selsected_meaning_tuple =(word, int_word_similiarity)
                    to_be_selsected_meaning_list.append(to_be_selsected_meaning_tuple)
                    # to_be_selsected_meaning_dict['word']=int_word_similiarity
                    # sorted_list=sorted(to_be_selsected_meaning_dict,key=lambda x: x[word],reverse=True)
                    # cn_meaning.append(sorted_list[0].keys()[0])
                sorted_list = sorted(to_be_selsected_meaning_list, key=lambda x: x[1], reverse=True)
                cn_meaning.append(sorted_list[0][0])
            else:
                cn_meaning.append('')

# 将列表转换为Pandas的数据框
df_word_level['cn_meaning']=cn_meaning
#将数据框写入Excel文件
df_word_level.to_excel('word_level_pos.xlsx', index=False)

# if __name__ == '__main__':
#     # my_str='n.衣服；服装|v.“clothe”的第三人称单数|网络服饰；衣物；各种衣物|'
#     # network_word_list=split_str_and_remove_network_word(my_str)
#     # print(network_word_list)
#     my_str='n.衣服；服装'
#     intact_pos_meaning=split_str_with_dot_and_semicolon(my_str)
#     print(intact_pos_meaning)
#
#

