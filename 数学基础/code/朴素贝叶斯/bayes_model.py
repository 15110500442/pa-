#测试数据
import numpy as np
#引入高斯朴素贝叶斯
from sklearn.naive_bayes import GaussianNB
#训练集
features_train = np.array([[2,1.9],[2,2.5],[3,3.4],[8,7.5],[7,8],[6,8.2]])
labels_train = np.array([1,1,1,2,2,2])
#实例化
clf = GaussianNB()
#训练数据 fit相当于trainclf.fit(features_train, labels_train)
#输出单个预测结果
clf.fit(features_train, labels_train)
features_test = np.array([[6.5,6.7]])#
pred = clf.predict(features_test)
print("预测的类别为:\t",pred)
