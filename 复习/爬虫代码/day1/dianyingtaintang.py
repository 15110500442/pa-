from bs4 import BeautifulSoup
import requests
import csv


def get_data(url,start,end):
    for page in range(start,end + 1):
        fullurl = url + 'list_23_%s.html'%page
        chuli(fullurl)
        #print(fullurl)

def chuli(fullurl):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    response = requests.get(fullurl,headers=header)
    response.encoding='gbk'
    html = response.text
    #print(respone.text)
    soup = BeautifulSoup(response.text,features='html.parser')
    a = soup.select('.co_content8 ul table')
    print(a)
    for i in a:
        title = i.select('.ulink')[0].get_text()
        time = i.select('font')[0].get_text()
        jianjie = i.select('tr td')[5].get_text()
        #print(title,time,jianjie)
        dict = {
        '电影名称':title,
        '发布时间及点击量':time,
        '简介': jianjie,
        }
        with open('dianying.csv','a') as f:
            name = ['电影名称','发布时间及点击量','简介']
            writer = csv.DictWriter(f,fieldnames=name)
            writer.writeheader()
            writer.writerow(dict)
















if __name__ == '__main__':
   start = int(input('请输入下载的开始页数（从1开始）:'))
   end = int(input("请输入下载的结束页数:"))
   url = 'http://dytt8.net/html/gndy/dyzz/'
   get_data(url,start,end)