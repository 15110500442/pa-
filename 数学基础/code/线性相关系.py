import math
#求期望
def get_EX(list):
    EX = 0
    for i in list:
        EX += i
    EX /= len(list)
    return EX
#print(get_EX(list))
#求方差
def get_DX(list):
    DX = 0
    EX = get_EX(list)
    for i in list:
        DX +=  (i - EX)**2
    DX /= len(list)
    return DX

#print(get_DX(list))
list_X = [0,1,2]
list_Y = [0,1,2.2]
#求（X,Y)的相关系数
cov_XY = 0  #协方差
list_XY = []
for x in range(len(list_X)):
    list_XY.append(list_X[x]*list_Y[x])
print(list_XY)
EXY = get_EX(list_XY)
EX = get_EX(list_X)
EY = get_EX(list_Y)

cov_XY = EXY - EX*EY
DX = get_DX(list_X)
DY = get_DX(list_Y)
R_XY = cov_XY/(math.sqrt(DX)*math.sqrt(DY))
print("相关系数为:\t",R_XY)



