import numpy as np
# import matplotlib.pyplot as plt
# X0 = np.mat([[3],
#             [2],
#             [1]])
X1 = np.mat([[1,2],
           [2,3],
            [3]])
X2 = np.mat([[2],
            [1],
            [2]])
# b = np.column_stack((X0,X1,X2,np.array(X1)**2,np.array(X1)*np.array(X2),np.array(X2)**2))
# print(b)
# X = np.array([[3,1,2],
#             [2,2,1],
#             [1,3,2]])
# def degree(A):
#     n = len(A[0:,-1])
#     print(n)
#     # if n == 2:
#     #     b = np.column_stack((X[:,0], X[:,1:2], X[:,2:3], np.array(X[:,1:2]) ** 2, np.array(X[:,1:2]) * np.array(X[:,2:3]), np.array(X[:,2:3]) ** 2))
#     #     print(b)
#     # elif n == 3:
#     #     c = np.column_stack((np.array(b),))
# degree(X)
def mapFeature(X1,X2,n):
    out_str = 'x0,'
    out = np.ones(X1.shape)
    for i in range(1,n+1):
        for j in range(0,i+1):
            out_str += 'X1^' + str((i-j)) + 'X2^' + str(j) + '\n'
            out = np.hstack((out, np.power(X1, (i - j)) * np.power(X2, j)))
    return out_str,out
# X1 = np.mat([[1]])
# X2 = np.mat([[2]])
out_str,out = mapFeature(X1.T, X2,2)
print(out)
print(out_str)

