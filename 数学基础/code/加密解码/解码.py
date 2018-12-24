import numpy as np
import re

C = []
gz_jz = []
for line in open('我发送的密文.txt'):
    gz_jz.append(int(re.sub('[\r\n\t]', '', line)))
    if len(gz_jz) == 4:
        C.append(gz_jz)
        gz_jz = []

K = np.mat([[1,0,1,3],[3,2,7,4],[1,9,2,1],[1,4,5,2]])#钥匙
str_jz = np.mat(C)*K.I#解谜



dict_str = {}
for line in open('密码本.txt'):
    dict_str[re.sub('[\r\n\t]', '', line.split(' ')[-1])] = line.split(' ')[0]

str_wb = []
for i in str_jz.flat:
    if str(int(round(i))) in dict_str:
        str_wb.append(dict_str[str(int(round(i)))])
print(''.join(str_wb))
