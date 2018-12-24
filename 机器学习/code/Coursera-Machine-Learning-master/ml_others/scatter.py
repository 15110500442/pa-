import numpy as np
import matplotlib.pyplot as plt
#读取数据
data = np.loadtxt("dataset_scatter.txt",delimiter=',')
x=data[:,0:2]
y=data[:,2]
pos = np.where(y==1)
neg = np.where(y==0)
plt.scatter(x[pos,0],x[pos,1],marker='s',c='r')
plt.scatter(x[neg,0],x[neg,1],marker='x',c='b')
plt.show()