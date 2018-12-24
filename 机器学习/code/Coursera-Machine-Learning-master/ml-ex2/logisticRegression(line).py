# 逻辑回归算法(决策边界为直线的情况)
# 假设函数:h(x)=theta0*x0+theta1*x1+theta2*x2
#
import matplotlib.pyplot as plt
import numpy as np
import random
# 初始化theta
# theta = np.zeros((3, 1))
# plt.plot([1,2,3])
# plt.show()
theta = np.mat([[-100],
                [10],
                [10]])
# theta = np.ones((3, 1))
iter_num = 50      #迭代次数
learningRate=0.005   #学习率
min_change = 1e-5    #阈值
# step1.加载数据并打印散点图
def printScatter(filename):
    # 读取数据
    data = np.loadtxt(filename, delimiter=',')
    x = data[:, 0:2]
    y = data[:, 2]
    pos = np.where(y == 1)
    neg = np.where(y == 0)
    plt.scatter(x[pos, 0], x[pos, 1], marker='s', c='r')
    plt.scatter(x[neg, 0], x[neg, 1], marker='x', c='b')
    # plt.show()
# printScatter("ex2data1_small.txt")
# step2.加载训练数据集(0,6)loadDataset(filename)
def loadDataset(filename, percent):
    data = np.loadtxt(filename, delimiter=',')
    np.random.shuffle(data)
    total = len(data)
    m = int(total * percent)
    X = data[:m, 0:2]
    Y = data[:m, -1].reshape(-1,1)
    rest_X = data[m:,0:2]
    temp = np.ones((total-m, 1)) # col 1
    rest_X = np.hstack((temp, rest_X))
    #add c 1
    rest_Y = data[m:,-1].reshape(-1,1)
    X0 = np.ones((m, 1))
    X = np.hstack((X0, X))
    n = X.shape[1]
    return X, Y, m, n,rest_X,rest_Y
X, Y, m, n,rest_X,rest_Y = loadDataset('ex2data1.txt', 0.6)
# step3.计算代价函数computeCost(theta,X,Y)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def computeCost(X, Y, theta):
    m = len(Y)
    z = sigmoid(np.dot(X, theta))
    z[z == 1] = 9e-18
    z[z == 0] = 1e-18
    J = - (np.dot(Y.T, np.log(z)) + np.dot((1 - Y).T, np.log(1 - z))) / m
    return J
J = computeCost(X, Y, theta)
# print("####.J######",J)
# step4.计算梯度computeDescent(theta,X,Y)
def computeDescent(theta, X, Y):
    # print("theta::",theta.shape)
    # print("X::", X.shape)
    # print("Y::", Y.shape)
    z = sigmoid(np.dot(X, theta))
    # print("z::", z.shape)
    gradient = np.dot(X.T,(z - Y))/m
    # print("gradient::", gradient.shape)
    return gradient
#print(computeDescent(theta,X,Y))
# step5.梯度下降函数gradientDescent(theta,X,Y,iter_num,learningRate)
def gradientDescent(theta,X,Y,iter_num,learningRate):
    i = 0
    J_list = []
    gradient = computeDescent(theta,X,Y)
    while (not np.all(np.absolute(gradient)<=min_change)) and (i<iter_num):
        theta = theta - learningRate*gradient
        gradient = computeDescent(theta, X, Y)
        J_list.append(computeCost(X, Y, theta))
        i += 1
        #print(i)
        #print("gradient",gradient)
    return theta,J_list,i
# step6.执行梯度下降函数
theta ,J_list,iter_num = gradientDescent(theta,X,Y,iter_num,learningRate)
print(theta,iter_num)
# step7.(附1:评价)生成代价函数(数值)与迭代次数(iter_num)的曲线
#print(J_list[0:200])
print('-----',np.arange(0,iter_num,1))
print('*****',np.array(J_list).reshape(iter_num,1))
plt.plot(np.arange(0,iter_num,1),np.array(J_list).reshape(iter_num,1),'-r')
# plt.plot([0,1,2,3,4],[24,24,24,24,24])
plt.show()
# step8.(附2:决策边界,绘图)决策边界printDecisionBoundary()
theta = np.array(theta)
theta0 = theta[0][0]
theta1 = theta[1][0]
theta2 = theta[2][0]
#打印散点图和拟合直线
# #打印散点图
plt.subplots(figsize=(100,100))
data = np.loadtxt("ex2data1.txt", delimiter=',')
x = data[:, 0:2]
y = data[:, 2]
pos = np.where(y == 1)
neg = np.where(y == 0)
plt.scatter(x[pos, 0], x[pos, 1], marker='s', c='r')
plt.scatter(x[neg, 0], x[neg, 1], marker='x', c='b')
#拟合直线
x  = list(np.linspace(0,100,101))
y = []
for i in range(len(x)):
    y.append((-theta0-theta1*x[i])/theta2)
plt.plot(x,y,color="red")
axes = plt.gca()
axes.legend(['decision boundary','dataset'])
# plt.show()
# step9.计算算法的分类准确度
#取出剩余的训练数据作为输入数据

predict_Y = sigmoid(np.dot(rest_X,theta))
predict_Y[predict_Y>=0.5] = 1
predict_Y[predict_Y<0.5] = 0
predict_data = predict_Y-rest_Y
print(len(predict_data[predict_data==0])/len(rest_Y))
plt.close('all')