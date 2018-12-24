import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

hidden_layer_size = 25
input_layer_size = 400
num_labels = 10

data = sio.loadmat('ex4data1.mat')
x = data['X']
y = data['y'] % 10
m = x.shape[0]
rand_indices = np.random.permutation(m)
sel = x[rand_indices[0:100]]
input('Program paused. Press enter to comtinue.\n')

data = sio.loadmat('ex4weights.mat')
Theta1 = data['Theta1']
Theta2 = data['Theta2']
# 合并theta

nn_params = np.append(Theta1, Theta2)
_lambda = 0


def sigmoid(z):
    return 1/(1 + np.exp(-z))


def nnCostFunction(nn_params,input_layer_size,hidden_layer_size,num_labels,x,y,_lambds):
    Theta1 = nn_params[0:hidden_layer_size * (input_layer_size + 1)].reshape(hidden_layer_size,input_layer_size + 1)
    Theta2 = nn_params[hidden_layer_size * (input_layer_size +1):].reshape(num_labels,hidden_layer_size +1)
    m = len(y)
    a1 = np.vstack((np.ones(m),x.T)).T
    a2 = sigmoid(np.dot(a1,Theta1.T))
    a2 = np.vstack((np.ones(m),a2.T)).T
    a3 = 

nnCostFunction(nn_params,input_layer_size,hidden_layer_size,num_labels,x,y,_lambda)




