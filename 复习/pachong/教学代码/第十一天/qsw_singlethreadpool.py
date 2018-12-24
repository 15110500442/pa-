#使用python3.2之后为我们封装的线程池
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests
import os
from lxml import etree
import re
#这个代码在获取小说列表、下载章节详情时候共同使用了线程池

def get_data(url):
    print('开始下载'+url)
    print(threading.current_thread().name)
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    # print(response.status_code)
    if response.status_code == 200:
        response.encoding = 'gbk'
        return response.text

def naveldone(future):
    #线程池执行设定任务结束后的结果参数
    print('下载完了'+ str(time.time()))
    text = future.result()
    #http://www.quanshuwang.com/book/161/161996
    #可以在这提取每一本书籍的连接
    html = etree.HTML(text)
    novallist = html.xpath('//ul[@class="seeWell cf"]/li')
    for novel in novallist:
        title = novel.xpath('.//a[@class="clearfix stitle"]/@title')[0]
        url = novel.xpath('.//a[@class="clearfix stitle"]/@href')[0]
        pattern = re.compile(r'.*?(\d+?).html',re.S)
        id = re.findall(pattern,url)[0]
        chapterurl = 'http://www.quanshuwang.com/book/%s/%s' % (id[:3],id)
        # http://www.quanshuwang.com/book/161/161996
        # http://www.quanshuwang.com/book_161996.html
        file_path = 'novel/'+title
        #判断当前文件夹是否存在
        if not os.path.exists(file_path):
            #如果不存在，则创建文件夹
            os.mkdir(file_path)
        get_chapter(chapterurl)

def get_chapter(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        response.encoding = 'gbk'
        get_chapter_done(response.text)

def get_chapter_done(text):
    #获取数据章节列表
    html = etree.HTML(text)
    chapter_detal_urls = html.xpath('//div[@class="clearfix dirconone"]/li/a/@href')
    add_chapterThreadpool(chapter_detal_urls)


#将每一个章节的下载任务添加进章节下载的线程池，执行下载任务
def add_chapterThreadpool(chapter_detal_urls):
    # global chapterdetailpool
    chapterdetailpool = ThreadPoolExecutor(20)
    for url in chapter_detal_urls:
        a = chapterdetailpool.submit(get_chapterDetal_data,url)
        a.add_done_callback(get_chapterDetal_data_done)
    chapterdetailpool.shutdown(True)

#下载章节详情的方法
def get_chapterDetal_data(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        response.encoding = 'gbk'
        # get_chapterDetal_data_done(response.text)
        return response.text

#章节下载完之后的回调
def get_chapterDetal_data_done(future):
    text = future.result()
    html = etree.HTML(text)
    shuming = html.xpath('//div[@id="direct"]/a[@class="article_title"]/text()')[0]
    zhangjieming =  html.xpath('//strong[@class="l jieqi_title"]/text()')[0]
    content = "".join(html.xpath('//div[@id="content"]/text()')).replace('<br />','').replace('\r','').replace('&nbsp;','')
    filename = 'novel/'+shuming+'/'+zhangjieming+'.txt'
    print(filename)
    with open(filename,'a') as f:
        f.write(content)

def main():
    #如何定义一个线程池(池子里面有三个创建好的线程，可以同时使用)
    #max_workers：这个参数是说，同时能够执行的最大的线程数
    srarttime = time.time()
    navalpool = ThreadPoolExecutor(20) # 获取每一页

    #如何提交任务给线程池呢？
    for i in range(1,10):
        #submit: 表示将我们需要执行的任务给这个线程池，
        url = 'http://www.quanshuwang.com/list/1_'+str(i)+'.html'
        a = navalpool.submit(get_data,url)
        #给线程池设置任务之后，可以设置一个回调函数，
        #作用是：当我们某个任务执行完毕之后，就会回调你设置的回调函数
        a.add_done_callback(naveldone)

    navalpool.shutdown(True)
    
    endtime = time.time()
    #如何设置才能让主线程等待子线程任务结束再结束
    print(threading.current_thread().name)
    print(endtime-srarttime)

if __name__ == '__main__':
    main()
