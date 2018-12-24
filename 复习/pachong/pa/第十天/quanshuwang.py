import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import os
import re
def get_data(url):
    print('开始下载'+ url)
    time.sleep(2)
    header = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    a = html.xpath('//ul[@class="seeWell cf"]')
    for i in a:
        title =i.xpath('.//a[@class="clearfix stitle"]/@title')[0]
        link = i.xpath('.//li/a/@href')[0]
        pattern = re.compile(r'.*?(\d+?).html', re.S)
        id = re.findall(pattern,link)[0]
        chapterurl = 'http://www.quanshuwang.com/book/%s/%s' % (id[:3], id)
        print(chapterurl)


        # file_path = 'novel1/' + title
        # if not os.path.exists(file_path):
        #     os.mkdir(file_path)
        # response = requests.get(chapterurl,headers=header)
        # print(response.text)
        # response.encoding = 'gbk'
        # html = etree.HTML(response.text)
        # print(html)
            # mulu = html.xpath('//div[@class="b-info"]')
            # for b in mulu:
            #
            #     link1 = b.xpath('.//a[@class="reader"]/@href')
            #     print(link1)
            #     for c in link1:
            #         response = requests.get('%s' %(c), headers=header)
            #         response.encoding = 'gbk'
            #         html = etree.HTML(response.text)
            #         zhangjie = html.xpath('//div[@class="clearfix dirconone"]')
            #         for d in zhangjie:
            #             zj = d.xpath('.//li/a/@href')


                        








    # print(response.status_code)
    # if response.status_code == 200:
    #     return response.status_code, url
def done(future):
    # 线程池执行设定任务结束后的结果参数
    print('下载完了')
    response = future.result()
    print(response)







def mian():
    pool = ThreadPoolExecutor(4)

    for i in range(1,2):
        url = 'http://www.quanshuwang.com/list/1_%s.html'%i
        handler = pool.submit(get_data,url)
        handler.add_done_callback(done)
    pool.shutdown(True)
    print(threading.current_thread().name)








if __name__ == '__main__':
    mian()