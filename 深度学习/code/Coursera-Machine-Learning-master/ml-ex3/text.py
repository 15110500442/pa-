import scipy.io
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.005  # 学习率
iteration_num =20000 # 迭代次数
min_Threshold = 1e-5  # 阈值

def loadDataset(filename):
    data = scipy.io.loadmat(filename)
    data_x = data['X']
    data_y = data['y']
    data = np.hstack((data_x,data_y))
    np.random.shuffle(data)
    totu = len(data)
    m = int(totu*0.7)
    x = data[:m,0:]
    Y = data[:m,-1].reshape(-1,1)
    x0 = np.ones((m,1))
    X = np.hstack((x0,x))
    print(X.shape)
    n = X.shape[1]
    theta = np.zeros((n, 1))  # 初始化theta
    return X,Y,m,n,theta
X,Y,m,n,theta = loadDataset('ex3data1.mat')

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
J = computerCost(X,Y,theta)

#step4 计算梯度computerDescent(theta,x,y)
def computerDescent(X,Y,theta):
    error = sigmoid(np.dot(X,theta))
    theta_gradient = np.dot(X.T, (error-Y)) / m
    return theta_gradient

theta_list = []
#step5 梯度下降 gradientDescent(theta,x,y,iter,learningRate)
def gradient_descent_iteration(X,Y,alpha,iteration_num,theta):
    gradient = computerDescent(X,Y,theta)
    i = 0
    a_list = []
    while (not np.all(np.absolute(gradient) <= min_Threshold)) and (i < iteration_num):
        theta = theta - alpha*gradient
        gradient = computerDescent(X, Y, theta)
        theta_list.append(list(computerCost(X,Y,theta)[0])[0])
        i +=1
    # theta_list.append(theta)
    return theta,a_list


theta_all = theta
iter = np.unique(Y,axis=0)
for i in iter:
    alpha *= 0.8
    Y_temp = np.copy(Y)
    Y_temp[Y_temp!=i] = 1
    Y_temp[Y_temp==i] = 0
    theta,a_list = gradient_descent_iteration(X,Y_temp,alpha,iteration_num,theta)
    theta_all = np.hstack((theta_all,theta))[:,1:]
    print(i)

    # print(theta_all)
# plt.plot(np.arange(0,iteration_num,1),np.array(theta_list).reshape(iteration_num,1),'-r')
print(theta_list)
plt.plot([i for i in range(iteration_num * 10)], theta_list)
plt.xlabel('Number of iterations')
plt.ylabel('Cost J')
plt.show()

# predict_data = sigmoid(np.dot(rest_xy,theta))
# predict_data[predict_data>=0.5]=1
# predict_data[predict_data<0.5]=0
# b = predict_data-rest_y
# print(len(b[b==0])/len(rest_y))