import pandas as pd
from unlimeted_translate import trans,translate_text

df = pd.read_excel('word_level_pos.xlsx')
#
# # print(df.to_string())
# guide_word_list=df['guideword'].astype(str).tolist()
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

'''
['', '', '', '但', '尽管', '还', '后', '动词之后', '强调', '因为', '', '不同的陈述', '', '工作', '', '数字', '使用', '正在或出现', '尽管', '喜欢', '较早', '避免某事', '直到', '解释原因', '', '', '', '', '', '门/窗', '公共场所', '停止操作', '靠近', '友好的', '相对的', '相似的', '关系', '小心', '结尾', '', '门/窗', '公共场所', '停止操作', '靠近', '友好的']
'''
import pandas as pd
#将trans_guide_word_list写入Excel
trans_guide_word_list=['', '', '', '但', '尽管', '还', '后', '动词之后', '强调', '因为', '', '不同的陈述', '', '工作', '', '数字', '使用', '正在或出现', '尽管', '喜欢', '较早', '避免某事', '直到', '解释原因', '', '', '', '', '', '门/窗', '公共场所', '停止操作', '靠近', '友好的', '相对的', '相似的', '关系', '小心', '结尾', '', '门/窗', '公共场所', '停止操作', '靠近', '友好的']

# 将列表转换为Pandas的数据框
df['guidword_cn']=trans_guide_word_list

# 将数据框写入Excel文件
df.to_excel('output.xlsx', index=False)
# df.to_excel('word_level_pos.xlsx', index=False)