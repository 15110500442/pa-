import threading
import time
from concurrent.futures import ThreadPoolExecutor
import re
import requests
from lxml import etree
import os

def get(url, data):
    print('开始下载' + url)
    print(threading.current_thread().name)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    response = requests.get(url, data, headers=header)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text


def chuli(future):
    # 线程池执行设定任务结束后的结果参数
    print('下载完了' + str(time.time()))
    text = future.result()
    html = etree.HTML(text)
    chulilist = html.xpath('//div[@class="newlist_list_content"]/table[@class="newlist"]')
    linklist = []
    for i in chulilist:
        if len(i) != 1:
            link = i.xpath('.//td[@class="zwmc"]/div/a[1]/@href')[0]
            #par = i.xpath('.//td[@class="zwmc"]/div/a[1]/@par')
            linklist.append(link)
    xiancheng2(linklist)


def xiancheng2(linklist):
    huoqu1 = ThreadPoolExecutor(4)
    for url in linklist:
        a = huoqu1.submit(get_quanbu,url)
        a.add_done_callback(quanbu_huidiao)
    huoqu1.shutdown(True)
def get_quanbu(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text


def quanbu_huidiao(future):
    text = future.result()
    c = etree.HTML(text)
    for i in c:
    # #//*[@id="clone_category"]/div[1]/div[1]/h1
         title = i.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')[0]
         #公司名字
         company_name = i.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()')
         #会员图标
         tupiao = i.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/img/@src')
         # file_path = '招聘信息/' + str(title)
         # if not os.path.exists(file_path):
         #    os.mkdir(file_path)

    html = re.compile(r'<div.*?class="terminalpage clearfix".*?<div.*?class="terminalpage-left".*?ul.*?class="terminal-ul clearfix".*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)<a.*?</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>.*?<span.*?id="span4freshdate">(.*?)</span>.*?</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>'
                      r'.*?<li.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>.*?</div>',re.S)
    a = re.findall(html,text)
    # d = '招聘信息/'+ str(title) + '/' + title+'.txt'
    # with open(d,'a')as f:
    #     f.write(str(a)+'\n')





def main():
    starttime = time.time()
    huoqu = ThreadPoolExecutor(4)
    for i in range(1, 10):
        url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        data = {
            'jl': '北京',
            'kw': '技术',
            'sm': 0,
            'p': '%s',
        }
        a = huoqu.submit(get, url, data)
        a.add_done_callback(chuli)
    huoqu.shutdown(True)
    print(threading.current_thread().name)


if __name__ == '__main__':
    main()
