# -*- coding:utf-8 -*-
#可以帮我们随机的获取UserAgent
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.chrome)
print(ua.ie)
print(ua.random)
