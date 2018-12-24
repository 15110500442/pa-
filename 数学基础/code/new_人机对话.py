'''
简单的人机对话程序
预处理（对答案进行分词，并加载到内存）
步骤一： 输入问题A
步骤二：对问题A进行分词
步骤三：对答案依次与list_seg_A进行相似度比较
步骤四：输出相似度最大的值对应的答案
'''
import NLP
nlp = NLP.NLP()
sim_min = 0.5   #相似度最小阈值
#答案库字典（（）,答案）
dict_answer = {}
#预处理（对答案进行分词，并加载到内存）
def str2tuple(segment):
    # tuple1 = ()
    # list_tmp = segment.split("/")
    # tuple1 = tuple(list_tmp)
    return tuple(segment[:-1].split("/"))
# 打开文件
file_abswer = open('dialog.txt',encoding='utf8')
# 计算相似度 交集/并集  set是可变集合
def computer_simimary(list_ask,list_questions):
    sim = 0
    # 交集
    num_jiaoji = len(set(list_ask)&set(list_questions))
    # 并集
    num_bingji = len(set(list_ask)|set(list_questions))
    if num_bingji !=0:
        sim = num_jiaoji/num_bingji
    return sim

for line in file_abswer:
    # print(line)
    list_line = line.split('###')
    # 字典dict_answer中的key，就是tuple_line
    tuple_line = str2tuple(nlp.Segment(list_line[0]))
    # 字典dict_answer中的value，就是answer_line
    answer_line = list_line[1]
    # 逐行加载到dict_answer
    dict_answer[tuple_line] = answer_line
# 关闭文件
file_abswer.close()
# 步骤1：输入问题a
question = input("请提问:")
tuple_ask = str2tuple(nlp.Segment(question))
# 步骤三：对答案依次与list_seg_A进行相似度比较y
finaly_answer = '我正在学习呢'
sim_max = 0
for k in dict_answer:
    sim = computer_simimary(set(tuple_ask),set(k))
    if sim>sim_max:
        sim_max = sim
        finaly_answer = dict_answer[k]
if sim_max >= sim_min:
    print("田静机器人-->",finaly_answer,"(", sim_max, ")")
else:
    print("田静机器人-->我现在在学习","(", sim_max, ")")



