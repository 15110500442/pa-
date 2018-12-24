import numpy as np
import random
#引入高斯朴素贝叶斯
from sklearn.naive_bayes import GaussianNB
import pandas as pd

def P_learn(iris_train, type_train,difference_list):
    clf = GaussianNB()
    clf.fit(iris_train, type_train)
    num = 1
    for i in difference_list:
        features_test = np.array([list(i)[:-1]])  #
        pred = clf.predict(features_test)
        if pred == i[-1]:
            num+=1
    P_learn = num / len(difference_list)*100
    return P_learn

def main():
    # iris_dic = {'Iris-setosa': 1, 'Iris-versicolor': 2, 'Iris-virginica': 3}
    a = pd.read_excel('iris.xlsx').values
    all = [list(i) for i in a]
    d = round(len(all)*0.6)
    b = random.sample(list(all),d)
    iris_list = [list(i)[:-1] for i in b]  # 115
    type_list = [list(i)[-1] for i in b]  # 1 2
    difference_list = [i for i in all if i not in b]
    iris_train = np.array(iris_list)
    type_train = np.array(type_list)
    P_learn(iris_train, type_train,difference_list)
    return P_learn(iris_train, type_train,difference_list)

x = 1
for i in range(100):
    x += main()
print(x / 100)
if __name__ == '__main__':
    main()

