#课堂练习
#求众数
#比如：1,2,2,3,3,4  的众数为 2与3
list1 = [1,2,2,3,3,4]
dict1={}  #字典dict1用来存储每个数字及其出现的次数

#步骤1、用字典dict来存储每个数及其对应的次数
        #1.1 如果元素在字典中不存在，则插入到字典dict中，并且value=1
        #1.2 如果元素已经存在于字典dict中，dict[key]+=1
for i in list1:
    if i not in dict1.keys():
        dict1[i] = 1 #1.1 如果元素在字典中不存在，则插入到字典dict中，并且value=1
    else:
        dict1[i] += 1 #1.2 如果元素已经存在于字典dict中，dict[key]+=1

print(dict1)
#步骤2、找出字典value的最大值m
m = 0
for i in dict1:
    if dict1[i]>m:
        m = dict1[i]
print(m)
#步骤3、输出打印字典dict中value=m的key
for i in dict1:
    if dict1[i] == m:
        print("众数",i,"次数",dict1[i])
