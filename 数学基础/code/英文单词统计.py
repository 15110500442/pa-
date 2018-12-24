#统计一篇英文文章中出现次数最多的单词
# 步骤：
# 1、打开文件，逐行读取并去除标点符号（编写去除标点符号的函数）
# 2、按空格分割，然后读取到字典中
# 3、对字典按频率进行倒排
# 4、输出前3个出现次数最多的单词
#定义并实现去除标点符号的函数
#定义标点符号列表
dict = {}   #字典
list_punctuation = [".",",","?","!"]
def punctuation_filter(str):
    for i in list_punctuation:
        str = str.replace(i," ")
    return str

file_article = open("英文.txt",encoding="utf8")
for line in file_article:
    #print(line)
    #调用去除标点符号的函数
    line = punctuation_filter(line)
    list_word = line.split(" ")
    for word in list_word:
        #print(word)
        # 把word读取到字典
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
file_article.close()
#print(dict)
#去除“”，“\n”
del dict[""]
del dict["\n"]
#对字典进行倒排
list_ret = sorted(dict.items(),key=lambda dict:dict[1],reverse=True)
print(list_ret)
# 3、打印输出前三个词
n = 0
for i in list_ret:
    if n>=3:
        break
    print(i[0],"***",i[1])
    n+=1