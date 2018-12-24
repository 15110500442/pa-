
import numpy as np
import matplotlib.pyplot as plt

m = 10 #训练集的个数
x0 = np.ones((m,1))
# print(x0)
x1 = np.arange(1,m+1).reshape(m,1)
# print(x1)
X = np.hstack((x0,x1)) # 矩阵相连接
# print(x)
Y = np.array([1.1,1.2,1.3,5,3,6,8,9,9.3,9.2]).reshape(m,1)
print(Y)
#学习率
alpha = 0.01
finaly_change = 1e-5
#代价函数
def computeCost(theta,X,Y):
    error = np.dot(X,theta) - Y
    J = (1/2/m)*np.dot(error.T,error)
    return J

#梯度下降函数
def gradientDescent(theta,X,Y):
    error= np.dot(X,theta) - Y
    theta_gradient = (1/m)*np.dot(X.T,error)
    return theta_gradient

def gradient_descent(X,Y,alpha):
    theta = np.array([1,1]).reshape(2,1)#初始值分别为1,1
    gradient = gradientDescent (theta,X,Y)
    while not np.all(np.absolute(gradient)<=finaly_change):
        theta = theta - alpha * gradient
        gradient = gradientDescent(theta,X,Y)
    return theta

#开始执行代码
theta = gradient_descent(X,Y,alpha)
print('theta:', theta)
print('cost:', computeCost(theta,X,Y))

plt.subplots(figsize=(10,10))
plt.scatter(x1,Y,marker='+')
x = np.linspace(0,11,10)
y = theta[0][0] + theta[1][0]*x
plt.plot(x,y,color="red")
axes = plt.gca()
axes.legend(['line regression','dataset'])
plt.show()