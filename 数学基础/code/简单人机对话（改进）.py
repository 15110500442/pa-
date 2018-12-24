import NLP
nlp = NLP.NLP()
sim_min = 0.5
#简单的人机对话
dict_dialog = {} #问题-答案 字典
dict_dialog_segment = {} #问题-答案_分词后 字典
#准备工作
#1.
    #1.1加载dialog.txt到字典中 dict_dialog = {}
def load_dialog(file_name):
    dict_dialog = {}
    file_dialog = open(file_name,encoding="utf8")
    for line in file_dialog:
        line_split = line.split("##n#")
        dict_dialog[line_split[0]] = line_split
    return dict_dialog

dict_dialog = load_dialog("dialog.txt")
#dict1 = {("姚明","身高","多少"):"226cm"}
#print(dict_dialog)
    #1.2 对dict_dialog字典中的key(问题),进行分词
def segment_key(dict,dict_seg):
    for key in dict:
        #对key进行分词
        #print(key)
        list_key = nlp.Segment(key)
        dict_seg[tuple(list_key)] = dict[key]

segment_key(dict_dialog,dict_dialog_segment)
dict_dialog.clear()
###print(dict_dialog_segment)  #问题-答案_分词后 字典
#2.问话 ask = input(),对问话进行分词
while True:
    ask = input("请提问")
    list_ask = nlp.Segment(ask)
    #print(list_ask)
    #一般来说 ，包括Jaccard及余弦夹角公式
    #3.1 Jaccard公式：比较list_ask与dict_dialog_segment字典中的key(问题)进行相似度计算
    def computer_sim_Jaccard(ask_list,question_list):
        num_jiaoji = len(set(ask_list)&set(question_list))
        num_bingji = len(set(ask_list)|set(question_list))
        if num_bingji == 0:
            return 0
        return num_jiaoji/num_bingji
    #3.2余弦夹角公式
    '''
    修改：莫某
    时间：2018-7-19 am 11:55
    func:
    why:
    '''
    def computer_sim_Cosin(ask_list,question_list):
        #ask_list = ["中国","首都","哪里"]
        #question_list_1 = ["中国","首都"]
        ask_set = set(ask_list)  #去除重复的元素
        question_set = set(question_list)
        union_set = ask_set|question_set #求并集
        ask_vector = []
        question_vector = []
        #生成ask_vector向量
        for i in union_set:
            if i in ask_set:
                ask_vector.append(1)
            else:
                ask_vector.append(0)
            if i in question_set:
                question_vector.append(1)
            else:
                question_vector.append(0)
        print(ask_vector)
        print(question_vector)
        print(question_set)
        #计算余弦夹角
        #[a,b],||a||,||b||
        neiji_ab = 0
        for i in range(len(ask_vector)):
            neiji_ab += ask_vector[i]*question_vector[i]
        length_a = 0
        for i in ask_vector:
            length_a += i**2
        length_a = length_a**0.5
        length_b = 0
        for i in question_vector:
            length_b += i ** 2
        length_b = length_b ** 0.5
        similary = 0
        if length_a !=0 and length_b!=0:
            similary = neiji_ab/(length_a*length_b)
        else:
            similary = 0
        return similary
    #4.输出相似度最大的key所对应的value(答案)
    #list_ask与dict_dialog_segment字典中的key(问题)进行相似度计算
    sim_max = 0
    finally_answer = "我不知道,正在学习呢"
    #version_n = get()
    for key in dict_dialog_segment:
        sim = computer_sim_Cosin(list_ask,list(key))
        #print(sim)
        if sim>sim_max:
            sim_max = sim
            finally_answer = dict_dialog_segment[key]
    if sim_max >= sim_min:
        print("机器人-->", finally_answer, "(", sim_max, ")")
    else:
        print("机器人-->我现在在学习")

