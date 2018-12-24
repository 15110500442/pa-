import numpy
import re
list_A = ["A1","A1","A2","A2","A1","A2"]
list_B = ["B1","B2","B3","B3","B4","B4"]
list_C = ["C1","C2","C3","C1","C1","C3"]

list_A_B = []
for i in range(len(list_A)):
    if i in range(0,len(list_B)):
        tuple_A_B = (list_A[i],list_B[i])
        list_A_B.append(tuple_A_B)
list_A_C = []
for i in range(len(list_A)):
    if i in range(0, len(list_C)):
        tuple_A_C = (list_A[i],list_C[i])
        list_A_C.append(tuple_A_C)
list_B_C = []
for i in range(len(list_B)):
    if i in range(0, len(list_C)):
        tuple_B_C = (list_B[i],list_C[i])
        list_B_C.append(tuple_B_C)
for str in list_B_C:
    print(str)
def Prob(X):
    #总个数
    n = 6
    count_X = 0
    find_obj = re.findall(r'([A-Z][0-9]+)', X)
    if len(find_obj) == 1:
        # 计算P(X)
        # 计算X的个数
        if X in list_A:
            count_X = list_A.count(X)
        if X in list_B:
            count_X = list_B.count(X)
        if X in list_C:
            count_X = list_C.count(X)
        #概率
        pro_X = count_X / n
        return pro_X
    if len(find_obj) == 2:
        X_2 = find_obj[0]
        Y_2 = find_obj[1]
        if X_2 in list_A and Y_2 in list_C:
            tup_X_Y = (X_2,Y_2)
            count_X = list_A_C.count(tup_X_Y)
        if X_2 in list_B and Y_2 in list_C:
            tup_X_Y = (X_2,Y_2)
            count_X = list_B_C.count(tup_X_Y)
            print(X_2,Y_2,count_X)
        #概率
        pro_XY = count_X / n
        print("pro_XY:",pro_XY)
        return pro_XY

def Prob_X_IN_Y(X,Y): #求条件概率P(X|Y) = P(XY)/P(Y)
    #计算P(XY)
    XY = X + Y
    pro_XY = Prob(XY)
    # print(pro_XY)
    #计算P(Y)
    pro_Y = Prob(Y)
    # print(pro_Y)
    pro_X_in_Y = pro_XY / pro_Y
    # print("pro_X_in_Y：",pro_X_in_Y)
    return pro_X_in_Y

def Prob_X_IN_Y_Z(X,Y,Z):#P(X|YZ) = ( P(YZ|X)*P(X) ) / P(YZ)
    #计算P(YZ)，因为Y与Z相互独立
    pro_YZ = Prob(Y) * Prob(Z)  ####
    #计算P(X)
    pro_X = Prob(X)
    #计算P(YZ|X) = P(Y|X)*P(Z|X)
    pro_Y_in_X = Prob_X_IN_Y(Y,X)
    pro_Z_in_X = Prob_X_IN_Y(Z,X)
    pro_YZ_in_X = pro_Y_in_X * pro_Z_in_X
    pro_X_in_Y_Z = pro_YZ_in_X * pro_X /pro_YZ   ###
    # print(pro_X_in_Y_Z)
    return pro_X_in_Y_Z

x2 = Prob_X_IN_Y_Z("C1","A1","B1")
x3 = Prob_X_IN_Y_Z("C2","A1","B1")
x4 = Prob_X_IN_Y_Z("C3","A1","B1")
print(x2,x3,x4)