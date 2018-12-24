#测试数据
import numpy as np
#引入高斯朴素贝叶斯
from sklearn.naive_bayes import GaussianNB
#训练集
features_train = np.array([[1,1],[1,2],[2,3],[2,3],[1,4],[2,4]])
labels_train = np.array([1,2,3,1,1,3])
#实例化
clf = GaussianNB()
#训练数据 fit相当于train
clf.fit(features_train, labels_train)
#输出单个预测结果
features_test = np.array([[1,3]])#
pred = clf.predict(features_test)
print("预测的类别为:\t",pred)
