from urllib.request import Request,urlopen
import urllib.parse
import ssl
#https://www.baidu.com/s?wd=%E8%B7%91%E8%BD%A6&pn=10&oq=%E8%B7%91%E8%BD%A6&tn=baiduhome_pg&ie=utf-8&usm=2&rsv_idx=2&rsv_pq=c25f90b800002c15&rsv


context = ssl._create_unverified_context()
url = 'https://www.baidu.com/s?'
page = int(input())