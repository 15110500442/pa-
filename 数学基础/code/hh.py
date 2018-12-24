import NLP
new_nlp = NLP.NLP()

dict_dialog = {} # 问题-答案  字典
dict_dialog_segment = {} # 问题-答案--分词后

def load_dialog(file_name):
    dict_dialog = {}
    file_dialog = open(file_name)
    for line in file_dialog:
        line_split = line.split("###")
        dict_dialog[line_split[0]] = line_split[1]
    return dict_dialog

dict_dialog = load_dialog('dialog.txt')

def segment_key(dict,dict_seg):
    print(dict)
    for key in dict:
        list_key = new_nlp.Segment(key)
        dict_seg[tuple(list_key)] = dict[key]
    #print(dict)
segment_key(dict_dialog,dict_dialog_segment)
dict_dialog.clear()

while True:
    ask = input("请提问")
    list_ask = new_nlp.Segment(ask)

