#求两个字符串的最大公共子串
#abc
str1 = "abcdex"
str2 = "mnabcyz"
list1 = []
for i in range(len(str1)+1):
    for j in range(len(str1)+1):
        if str1[i:j]!='':
            list1.append(str1[i:j])
max_str = list1[0]
for i in list1:
    if i in str2:
        if len(i)>len(max_str):
            max_str = i
print(max_str)


print(list1)