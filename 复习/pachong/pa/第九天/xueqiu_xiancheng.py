import json
import queue
import threading

import requests
from lxml import etree

dict = {}
list = []
url = 'https://xueqiu.com/today#/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Cookie': 'aliyungf_tc=AQAAAEy+mD/Wkw4A5s7KfKa6mfK1WEWj; xq_a_token=019174f18bf425d22c8e965e48243d9fcfbd2cc0; xq_a_token.sig=_pB0kKy3fV9fvtvkOzxduQTrp7E; xq_r_token=2d465aa5d312fbe8d88b4e7de81e1e915de7989a; xq_r_token.sig=lOCElS5ycgbih9P-Ny3cohQ-FSA; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528716588; _ga=GA1.2.1484728698.1528716608; _gid=GA1.2.797597493.1528716608; u=211528716742923; device_id=845bb9a7abdc062cdbc308fa48853961; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1528761415; _gat_gtag_UA_16079156_4=1'
}


def pa():
    response = requests.get(url, headers=header)
    page_html = etree.HTML(response.text)
    a = page_html.xpath('//router-link[@class="tab__item"]/text()')
    b = page_html.xpath('//@data-category')
    dict[str(a)] = b
    list.append(b)
    # print(dict)


pa()


class Huoqu(threading.Thread):
    def __init__(self, threaname, pagequeue, dataqueue):
        super(Huoqu, self).__init__()
        self.threaname = threaname
        self.pagequeue = pagequeue
        self.dataqueue = dataqueue

    # print(self.threaname)
    def run(self):
        print('开启' + self.threaname)
        for k, v in dict.items():
            for item in v:
                url1 = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=%s' % item
                rep = requests.get(url1, headers=header)
                # print(rep.status_code)
                if rep.status_code == 200:
                    self.dataqueue.put(rep.text)
                    # print( self.dataqueue,type(self.dataqueue))
                # print('run起来')


class Threadparse(threading.Thread):
    def __init__(self, threaname, dataqueue, lock):
        super(Threadparse, self).__init__()
        self.threaname = threaname
        self.dataqueue = dataqueue
        self.lock = lock

    def run(self):
        while not self.dataqueue.empty():
            rep = self.dataqueue.get()
            # print(rep)
            print('获取到了')
            self.jiexi(rep)

    def jiexi(self, rep):
        rep1 = rep.replace("'", '"')
        data = json.loads(rep1)
        data1 = data['list']
        for item in data1:
            try:
                data = json.loads(item['data'])
                id = str(data['id'])
                title = str(data['title'])
                miaosu = str(data['description'])
                user = str(data['user']['screen_name'])
                column = str(item['column'])
                touxiang = str(data['user']['profile_image_url'])
                link = str(data['target'])
                print(id, title, miaosu, user, column, touxiang, link)
                dict1 = {
                    'id': id,
                    'title': title,
                    'miaosu': miaosu,
                    'user': user,
                    'column': column,
                    'touxiang': touxiang,
                    'link': link
                }
                self.lock.acquire()
                with open('duanzieee.json', 'a') as f:
                    f.write(json.dumps(dict1, ensure_ascii=False) + '\n')
                self.lock.release()

            except:
                data = json.loads(item['data'])
                miaosu = str(data['text'])
                column = str(item['column'])
                link = str(data['target'])
                print(miaosu, column, link)


def main():
    pagequeue = queue.Queue(10)
    dataqueue = queue.Queue()
    xiancheng = ['线程1', '线程2', '线程3']
    b = []
    for threaname in xiancheng:
        threa = Huoqu(threaname, pagequeue, dataqueue)
        threa.start()
        b.append(threa)

    for threa in b:
        threa.join()
    lock = threading.Lock()
    parse = ['含青一号', '含青二号', '含青三号']

    c = []
    for thread in parse:
        parse1 = Threadparse(thread, dataqueue, lock)
        parse1.start()
        c.append(parse1)
    for threa in c:
        threa.join()


if __name__ == '__main__':
    main()
