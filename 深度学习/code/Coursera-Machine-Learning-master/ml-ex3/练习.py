import scipy.io
import numpy as np
import matplotlib.pyplot as plt

def loadDataset(filename):
    data = scipy.io.loadmat(filename)
    data_x = data['X']
    data_y = data['y']
    totu = len(data_x)
    m = int(totu*0.8)
    x = data_x[4,:]
    print(x.shape)
#     Y = data_y[:m,-1]
#     x0 = np.ones((m, 1))
#     X = np.hstack((x0,x))
#     print(X.shape)
#
# #     n = X.shape[1]
# #     theta = np.zeros((n,1))  # 初始化theta
#     return X,Y,m,theta
loadDataset('ex3data1.mat')
#
# #sigmoid假设函数
# def sigmoid(z):
#     return 1/(1+np.exp(-z))
#
# #step3 计算代价函数computerCost(theta,x,y)
# def computerCost(X,Y,theta):
#     # print('y',Y.shape)
#     # print('theta',theta.shape)
#     a = np.dot(X,theta)
#     z = sigmoid(a)
#     z[z==1]=9e-18
#     z[z==0]=1e-18
#     J = -(1/m)*(np.dot(Y,np.log(z)) + np.dot((1-Y),np.log(1-z)))
#     return J
# J = computerCost(X,Y,theta)
# iter = len(np.unique(Y,axis=0))
# for

