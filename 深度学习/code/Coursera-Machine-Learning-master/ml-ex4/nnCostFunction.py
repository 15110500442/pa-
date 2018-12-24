import numpy as np
from sigmoid import sigmoid
from sigmoidGradient import sigmoidGradient

# NNCOSTFUNCTION为两层实现神经网络成本函数
# NNCOSTFUNCTION Implements the neural network cost function for a two layer

# 神经网络执行分类
# neural network which performs classification

# 计算神经网络的成本和梯度
#   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
#   X, y, lambda) computes the cost and gradient of the neural network. The

# 神经网络的参数被“展开”到矢量中
#   parameters for the neural network are "unrolled" into the vector

# nn_params并需要转换回权重矩阵
#   nn_params and need to be converted back into the weight matrices.

# 返回的参数grad应该是一个“展开”的向量
#   The returned parameter grad should be a "unrolled" vector of the

# 神经网络的偏导数
#   partial derivatives of the neural network.

#
def nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, _lambda):
    # Reshape nn_params回到参数Theta1和Theta2，即权重矩阵
    # Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices

    # 为我们的2层神经网络
    # for our 2 layer neural network
    Theta1 = nn_params[0:hidden_layer_size * (input_layer_size + 1)].reshape(\
                 hidden_layer_size, input_layer_size + 1)
    print(Theta1.shape)
    Theta2 = nn_params[hidden_layer_size * (input_layer_size + 1):].reshape(\
                 num_labels, hidden_layer_size + 1)

    # Setup some useful variables
    m = len(y) # number of training examples

    # ====================== YOUR CODE HERE ======================
    # Instructions: You should complete the code by working through the
    #               following parts.
    #
    # Part 1: Feedforward the neural network and return the cost in the
    #         variable J. After implementing Part 1, you can verify that your
    #         cost function computation is correct by verifying the cost
    #         computed in ex4.m
    #
    # Part 2: Implement the backpropagation algorithm to compute the gradients
    #         Theta1_grad and Theta2_grad. You should return the partial derivatives of
    #         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
    #         Theta2_grad, respectively. After implementing Part 2, you can check
    #         that your implementation is correct by running checkNNGradients
    #
    #         Note: The vector y passed into the function is a vector of labels
    #               containing values from 1..K. You need to map this vector into a 
    #               binary vector of 1's and 0's to be used with the neural network
    #               cost function.
    #
    #         Hint: We recommend implementing backpropagation using a for-loop
    #               over the training examples if you are implementing it for the 
    #               first time.
    #
    # Part 3: Implement regularization with the cost function and gradients.
    #
    #         Hint: You can implement this around the code for
    #               backpropagation. That is, you can compute the gradients for
    #               the regularization separately and then add them to Theta1_grad
    #               and Theta2_grad from Part 2.
    '''
        ＃======================你的代码在这里======================
    ＃说明：您应该通过完成代码来完成代码以下部分。
    ＃第1部分：前馈神经网络并返回成本
    #variable J.实施第1部分后，您可以验证您的
    通过验证成本，＃cost function calculation是正确的
    ＃在ex4.m中计算
    ＃
    ＃第2部分：实现反向传播算法来计算梯度
    ＃Theta1_grad和Theta2_grad。你应该返回的偏导数
    #Theta1_grad和Theta1中的Theta1和Theta2的成本函数
    ＃Theta2_grad，分别。实施第2部分后，您可以检查
    ＃通过运行checkNNGradients实现正确的＃
    ＃
    ＃注意：传递给函数的向量是标签向量
    ＃包含1..K的值。您需要将此向量映射到a
    ＃与神经网络一起使用的1和0的二进制向量
    #cost function。
    ＃
    ＃提示：我们建议使用for循环实现反向传播
    ＃如果你正在为它实现训练样例
    ＃ 第一次。
    ＃
    ＃第3部分：使用成本函数和梯度实现正则化。
    ＃
    ＃提示：你可以围绕代码实现这个
    #backpropagation。也就是说，您可以计算渐变
    分别＃正则化，然后将它们添加到Theta1_grad
    ＃和第2部分中的Theta2_grad。
    
    '''
    a1 = np.vstack((np.ones(m), X.T)).T
    a2 = sigmoid(np.dot(a1, Theta1.T))
    a2 = np.vstack((np.ones(m), a2.T)).T
    a3 = sigmoid(np.dot(a2, Theta2.T))
    y = np.tile((np.arange(num_labels)+1)%10,(m,1)) == np.tile(y,(1,num_labels))

    regTheta1 = Theta1[:,1:]
    regTheta2 = Theta2[:,1:]

    J = -np.sum( y * np.log(a3) + (1-y) * np.log(1-a3) ) / m + \
        _lambda * np.sum(regTheta1*regTheta1) / m/2 + \
        _lambda * np.sum(regTheta2*regTheta2) / m/2

    delta1 = np.zeros(Theta1.shape)
    delta2 = np.zeros(Theta2.shape)
    for i in range(m):
        a1_ = a1[i]; a2_ = a2[i]; a3_ = a3[i]
        d3 = a3_ - y[i]; d2 = np.dot(d3,Theta2) * sigmoidGradient(np.append(1,np.dot(a1_, Theta1.T)))
        delta1 = delta1 + np.dot(d2[1:].reshape(-1,1),a1_.reshape(1,-1)); 
        delta2 = delta2 + np.dot(d3.reshape(-1,1), a2_.reshape(1,-1))

    regTheta1 = np.vstack((np.zeros(Theta1.shape[0]), regTheta1.T)).T
    regTheta2 = np.vstack((np.zeros(Theta2.shape[0]), regTheta2.T)).T
    Theta1_grad = delta1 / m + _lambda * regTheta1 / m
    Theta2_grad = delta2 / m + _lambda * regTheta2 / m

    grad = np.append(Theta1_grad.flatten(), Theta2_grad.flatten())
    print('cost value: %lf'%J)
    
    return J, grad