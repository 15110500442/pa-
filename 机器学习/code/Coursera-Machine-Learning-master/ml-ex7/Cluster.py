import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
#step1.画出散点图
data = sio.loadmat('ex7data2.mat')
X = data['X']
m,n = X.shape
print("X.shape:",m,n)
x = X[:,0]  #第1列
y = X[:,1]  #第2列
plt.scatter(x,y,marker='x')
plt.show()
#step2.k=2,3,...m-1
#k = np.arange(2,m) #n=2,3,...m-1
k = np.arange(2,8) #n=2,3,...m-1
#step3.分别计算当k=2,3,...m-1相应的代价函数,画出肘部曲线
def findClosestCentroids(X, centroids):
    # Set K
    J_cost = 0
    K = centroids.shape[0]
    # You need to return the following variables correctly.
    idx = np.zeros(X.shape[0])
    for i in range(X.shape[0]):
        min = np.inf
        for j in range(K):
            diff = np.sum(np.power(X[i,:] - centroids[j,:], 2))
            if min > diff:
                min = diff
                idx[i] = j
                J_cost += min
    idx = idx.astype(int)
    return idx,J_cost
J_cost_k = [] #代价函数
for i in k:
    X_shuffle = np.random.permutation(X)  # 返回副本
    centroid = X_shuffle[:i,0:2]
    idx,J_cost = findClosestCentroids(X,centroid)
    #print(idx)
    J_cost_k.append(J_cost)

#step4.画出肘部曲线
plt.plot(list(np.asarray(k).reshape(len(k),1)),J_cost_k,'-r')
plt.show()
#step5.根据肘部曲线选择K(比如k=3)
#step6.根据K进行聚类(多次选择k个初始点,选择代价函数最小的
#聚类中心 )
J_min = np.inf
centroid = np.zeros((3,2))
for i in range(10):
    X_shuffle = np.random.permutation(X)  # 返回副本
    centroid_tmp = X_shuffle[:3, 0:2]
    idx, J_cost = findClosestCentroids(X, centroid_tmp)
    if J_min>J_cost:
        J_min = J_cost
        centroid = centroid_tmp
idx, J_cost = findClosestCentroids(X, centroid)
#print(idx)
#step7.绘制散点图
y = np.asarray(idx).reshape(300,1)
data = np.hstack((X,y))
x = data[:, 0:2]
y = data[:, 2]
pos_0 = np.where(y == 0)
pos_1 = np.where(y == 1)
pos_2 = np.where(y == 2)
plt.plot(x[pos_0][:, 0], x[pos_0][:, 1], 'k+',color="red", linewidth=2, markersize=7)
plt.plot(x[pos_1][:, 0], x[pos_1][:, 1], 'k*',color="blue", linewidth=2, markersize=7)
plt.plot(x[pos_2][:, 0], x[pos_2][:, 1], 'ko', color="green",markerfacecolor='y', markersize=7)
plt.show()








