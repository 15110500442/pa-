import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor
import threading


def qaqu_syan(url, headers):
    reques = requests.get(url, headers=headers)
    with open('简书摄影页信息.txt', 'w', encoding='utf-8') as f:
        f.write(reques.text)


def sheyan_jianxi():
    navalpool = ThreadPoolExecutor(5)
    w = '[图片]https://www.jianshu.com'
    with open('简书摄影页信息.txt', 'r', encoding='utf-8') as f:
        q = f.read()
    html = etree.HTML(q)
    qichazjjia = html.xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li')
    for i in qichazjjia:
        wenjialj = i.xpath('./div/a/@href')
        url = w + wenjialj[0]
        a = navalpool.submit(paquwzhao, url)
        a.add_done_callback(wenzhao_jianxi)
    navalpool.shutdown(True)


def paquwzhao(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    print('开始请求文章')
    requ = requests.get(url, headers=headers)
    print(requ.status_code)
    return requ.text


def wenzhao_jianxi(future):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    text = future.result()
    html = etree.HTML(text)
    wenzhaodiv = html.xpath('/html/body/div[1]/div[1]/div[1]/h1/text()')
    name = html.xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/span/a/text()')
    shijain = html.xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/div/span[1]/text()')
    wenzhaxqin = html.xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/p/text()')
    tupain = html.xpath('//div[@class="image-view"]/img/@data-original-src')
    print(tupain)
    try:
        os.mkdir(str(wenzhaodiv))
        with open(str(wenzhaodiv) + '/' + name[0] + '.txt', 'a', encoding='utf-8') as f:
            f.write(shijain[0] + '\n')
            f.write(wenzhaxqin[0])
        xxx = 1
        for i in tupain:
            xxx += 1
            requ = requests.get('http:' + '%s' % i, headers=headers)
            print(requ.status_code)
            with open(str(wenzhaodiv) + '/' + '%s' % xxx + '.jpg', 'wb') as f:
                f.write(requ.content)
    except:

        with open(str(wenzhaodiv) + '/' + name[0] + '.txt', 'a', encoding='utf-8') as f:
            f.write(shijain[0] + '\n')
            f.write(wenzhaxqin[0])
        xxx = 1
        for i in tupain:
            xxx += 1
            requ = requests.get('http:' + '%s' % i, headers=headers)
            print(requ.status_code)
            with open(str(wenzhaodiv) + '/' + '%s' % xxx + '.jpg', 'wb') as f:
                f.write(requ.content)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}
url = '[图片]https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop'
if __name__ == '__main__':
    qaqu_syan(url,headers)
    sheyan_jianxi()