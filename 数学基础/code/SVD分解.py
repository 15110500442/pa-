#!/usr/bin/python
#  -*- coding:utf-8 -*-
from PIL import Image
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def restore1(u, sigma, v, k):
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    # 重构图像
    a = np.dot(u[:, :k], np.diag(sigma[:k])).dot(v[:k, :])
    # 上述语句等价于：
    # for i in range(k):
    #     ui = u[:, i].reshape(m, 1)
    #     vi = v[i].reshape(1, n)
    #     a += sigma[i] * np.dot(ui, vi)
    a[a < 0] = 0
    a[a > 255] = 255
    return np.rint(a).astype('uint8')

#1)首先读取一张图片
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False
A = Image.open('svd.png')
a = np.array(A)  # 转换成矩阵
#2）然后可以利用python的numpy库对彩色图像的3个通道进行SVD分解：
# 由于是彩色图像，所以3通道。a的最内层数组为三个数，分别表示RGB，用来表示一个像素
u_r, sigma_r, v_r = np.linalg.svd(a[:, :, 0])
u_g, sigma_g, v_g = np.linalg.svd(a[:, :, 1])
u_b, sigma_b, v_b = np.linalg.svd(a[:, :, 2])
#3）然后便可以根据需要压缩图像
# （丢弃分解出来的三个矩阵中的数据），
# 利用的奇异值个数越少，则压缩的越厉害。
# 不同程度压缩后，重构图像的清晰度：
plt.figure(facecolor='w', figsize=(10, 10))
# 奇异值个数依次取：1,2,...,12。看效果
K = 12
for k in range(1, K + 1):
    print(k)
    R = restore1(u_r, sigma_r, v_r, k)
    G = restore1(u_g, sigma_g, v_g, k)
    B = restore1(u_b, sigma_b, v_b, k)
    I = np.stack((R, G, B), axis=2)
    # 将图片重构后的显示出来
    plt.subplot(3, 4, k)
    plt.imshow(I)
    plt.axis('off')
    plt.title(u'奇异值个数：%d' % k)

plt.suptitle(u'SVD与图像分解', fontsize=20)
plt.tight_layout(0.1, rect=(0, 0, 1, 0.92))
plt.show()
