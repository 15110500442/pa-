import numpy as np
data =np.loadtxt('ex1data1.txt',delimiter=',')
x = data[:,1]
y = data[:,-1]
print(x)
print(y)