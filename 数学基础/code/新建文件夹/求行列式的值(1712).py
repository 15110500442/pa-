import numpy as np
from numpy.linalg import*
#行列式a
a = np.array([[1,2,-5],
             [-2,0,2],
             [1,0,0]])
print(det(a))#求a的行列式的值