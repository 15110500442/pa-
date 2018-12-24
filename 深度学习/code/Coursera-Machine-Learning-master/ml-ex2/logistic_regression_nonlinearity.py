import numpy as np
import matplotlib.pyplot as plt
#逻辑回归算法（决策边界为非线性的情况）
#假设函数 h(x) = theta0*x0+theta1*x1+theta2*x2
#logistic_Regression_Line
# 初始化theta
theta = np.zeros((10, 1))
# 学习率
alpha = 0.01
# 迭代次数
iteration_num = 200000
# 阈值
min_Threshold = 1e-5
# 高阶算法
def mapFeature(X, n):
    X1 = X[:,1].reshape(-1, 1)
    X2 = X[:,2].reshape(-1, 1)
    map_X = np.zeros((len(X), 1))
    num = 0
    for i in range(0, n + 1):
        for j in range(0, n - i + 1):
            num += 1
            temp = X1 ** i * X2 ** j
            map_X = np.hstack((map_X, np.array(temp).reshape(-1, 1)))
    return map_X[:,1:]


#step1 加载数据并打印散点图
def printScatter(filename):
    data = np.loadtxt(filename,delimiter=',')
    x = data[:,0:2]
    y = data[:,2]
    pos = np.where(y == 1)
    meg = np.where(y == 0)
    plt.scatter(x[pos,0],x[pos,1],marker='s',c='r')
    plt.scatter(x[meg,0],x[meg,1],marker='x',c='b')
    plt.show()
#printScatter("ex2data2.txt")


# #step2 计算训练加载数据集（x,y）
def loadDataset(filename):
    data = np.loadtxt(filename,delimiter=',')
    np.random.shuffle(data)
    totu = len(data)
    m = int(totu*0.9)
    x = data[:m,0:2]
    Y = data[:m,-1]
    temp = np.ones((totu-m,1))
    rest_x = data[m:, 0:2]
    rest_y = data[m:,-1].reshape(-1,1)
    rest_xy = np.hstack((temp,rest_x))
    x0 = np.ones((m,1))
    X = np.hstack((x0,x))
    n = X.shape[1]
    return X,Y,m,n,rest_xy,rest_y
X,Y,m,n,rest_xy,rest_y=loadDataset("ex2data2.txt")


#矩阵扩展为3阶多项式矩阵
X = mapFeature(X,3)

#sigmoid假设函数
def sigmoid(z):
    return 1/(1+np.exp(-z))


#step3 计算代价函数computerCost(theta,x,y)
def computerCost(X,Y,theta):
    a = np.dot(X,theta)
    z = sigmoid(a)
    z[z==1]=9e-18
    z[z==0]=1e-18
    J = -(1/m)*(np.dot(Y.T,np.log(z)) + np.dot((1-Y).T,np.log(1-z)))
    return J

computerCost(X,Y,theta)
#step4 计算梯度computerDescent(theta,x,y)
def computerDescent(X,Y,theta):
    error = sigmoid(np.dot(X,theta)) - Y.reshape(m,1)
    theta_gradient = np.dot(X.T, error) / m
    return theta_gradient


#step5 梯度下降 gradientDescent(theta,x,y,iter,learningRate)
def gradient_descent_iteration(X,Y,alpha,iteration_num,theta):
    gradient = computerDescent(X,Y,theta)
    i = 0
    a_list = []
    while (not np.all(np.absolute(gradient) <= min_Threshold)) and (i < iteration_num):
        theta = theta - alpha*gradient
        gradient = computerDescent(X, Y, theta)
        a_list.append(computerCost(X,Y,theta))
        i +=1
    return theta,a_list

# #step6 执行梯度下降函数
theta,a_list = gradient_descent_iteration(X,Y,alpha,iteration_num,theta)
print(theta)

#step7 （附1:评价）生成代价函数（数值）与迭代次数（iter）的曲线
plt.plot(np.arange(0,iteration_num,1),np.array(a_list).reshape(iteration_num,1),'-r')
plt.xlabel('Number of iterations')
plt.ylabel('Cost J')
plt.show()

#step8 （附2:决策边界）绘制决策边界
def plot_desicion_boundary(x,Y,theta):
    data = np.loadtxt('ex2data2.txt',delimiter=',')
    plt.subplots(figsize=(10,10))
    x = data[:, 0:2]
    y = data[:, 2]
    pos = np.where(y == 1)
    meg = np.where(y == 0)
    plt.scatter(x[pos, 0], x[pos, 1], marker='s', c='r')
    plt.scatter(x[meg, 0], x[meg, 1], marker='x', c='b')
    u = np.linspace(-1,1,50)
    v = np.linspace(-1,1,50)
    z = np.zeros((u.shape[0], v.shape[0]))
    for i in range(0,u.shape[0]):
        for j in range(0,v.shape[0]):
            z[i,j] =np.dot(theta.T,mapFeature(np.hstack((np.mat(1),np.mat(u[i]),np.mat(v[j]))),3).reshape(10,1))
    u, v = np.meshgrid(u, v)
    plt.contour(u, v, z.T, (0,), colors='g', linewidths=2)
    plt.show()
plot_desicion_boundary(X,Y,theta)


# step9计算准确度
# 剩余的数据训练数据作为输入数据
rest_e = mapFeature(rest_xy,3)
predict_data = sigmoid(np.dot(rest_e,theta))
predict_data[predict_data>=0.5]=1
predict_data[predict_data<0.5]=0
Train_Accuracy = predict_data-rest_y
print('Train Accuracy: %.2f'%(len(Train_Accuracy[Train_Accuracy==0])/len(rest_y)* 100)+' %')

