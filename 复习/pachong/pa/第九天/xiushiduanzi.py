import threading
import queue
import json
import requests
from lxml import etree

class ThreadCrawl(threading.Thread):
    def __init__(self, threaname,pagequeue,dataqueue):
        # 继承父类方法
        super(ThreadCrawl, self).__init__()
        self.threaname = threaname
        self.pagequeue = pagequeue
        self.dataqueue = dataqueue
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        print(self, threaname)

    # 重写父类的方法
    def run(self):
        while not self.pagequeue.empty():
            print('开启'+self.threaname)
            #获取页码
            page = self.pagequeue.get()
            #拼接网址
            fullurl = 'https://www.qiushibaike.com/8hr/page/'+ str(page)+'/'
            #发起请求，获取响应结果
            response = requests.get(fullurl,headers=self.header)
            print(response.status_code)
            if response.status_code == 200:
                self.dataqueue.put(response.text)
            #print( self.dataqueue,type(self.dataqueue))
            print('run起来')
class Threadparse(threading.Thread):
    def __init__(self,threaname,dataqueue,lock):
        super(Threadparse, self).__init__()
        self.threaname = threaname
        self.dataqueue = dataqueue
        self.lock = lock
    def run(self):
        #解析获取的数据
        #队列
        while not self.dataqueue.empty():
            html = self.dataqueue.get()
            print('获取到了')
            self.jiexi(html)
    def jiexi(self,html):
        d = etree.HTML(html)
        flist = d.xpath('//div[@id="content-left"]/div')
        for i in flist:
            title = i.xpath('.//h2/text()')
            content = i.xpath('.//div[@class="content"]/span/text()')
            print(title,content)
            dict = {
                'title':title,
                'content':content,
            }
            self.lock.acquire()
            with open('duanzi.json','a') as f:
                f.write(json.dumps(dict,ensure_ascii=False) + '\n')
            self.lock.release()


# 主线程
def mian():
    # 创建一个任务队列
    pagequeue = queue.Queue(30)
    #创建一个数据队列,将获取的结果
    dataqueue = queue.Queue()
    for i in range(1, 14):
        # 往任务队列中存要请求的页码
        pagequeue.put(i)

    # 创建线程来获取网页的内容
    crawlnanes = ['田静一号', '田静二号', '田静三号']
    b = []
    for threaname in crawlnanes:
        threa = ThreadCrawl(threaname,pagequeue,dataqueue)
        threa.start()
        b.append(threa)

    for threa in b:
        threa.join()
    lock = threading.Lock()
    #创建一个解析的线程
    parse = ['含青一号', '含青二号', '含青三号']

    c=[]
    for thread in parse:
        parse1 = Threadparse(thread,dataqueue,lock)
        parse1.start()
        c.append(parse1)
    for threa in c:
        threa.join()

    print(threading.current_thread().name)
if __name__ == '__main__':
    mian()
