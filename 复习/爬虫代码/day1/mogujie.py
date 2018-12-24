import requests
import json
import re
from bs4 import BeautifulSoup
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36'
}
url ='http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery21105355664687746757_1528449406507&pids=109499,109520,109731,109753,110549,109779,110548,110547,109757,109793,109795,110563,110546,110544&_=1528449406511'
a = requests.get(url,headers=header)
com_data = a.text.replace('jQuery21105355664687746757_1528449406507','').replace('(','').replace(')','').replace("'",'"')
com_list = json.loads(com_data)
dict = {}
for k in com_list['data'].keys():
    for item in com_list['data'][k]['list']:
        title = item['title']
        link = item['link']
        dict[title] = link
print(dict.keys())
sousuo = input('请输入你要搜索的名字:')
print(dict[sousuo])
print(com_list)
#http://list.mogujie.com/book/clothing/50240?acm=3.
cids = re.compile(r'http://list.mogujie.com/book/.*?/(\d*?){1}.acm=',re.S)
cid = re.findall(cids,str(dict[sousuo]))
start = int(input('请输入起始页'))
end = int(input('请输入起始页'))
p = 0
for foo in range(start,end+1):
    wantUrl = 'http://list.mogujie.com/search?cKey=15&page=%s&sort=pop&ad=0&fcid=%s'%(foo,cid[0])
    wantResponse = requests.get(wantUrl)
    wantText = wantResponse.text
    wantText = json.loads(wantText)
    p += len(wantText['result']['wall']['docs'])
    for i in wantText['result']['wall']['docs']:
        print('商品名:%s\n原价格:%s元\n现价:%s元\n图片:%s\n链接:http:%s' %
                (i['title'], i['orgPrice'], i['price'], i['img'], i['link'])
                  )
        print()
    print('共搜到%s件商品!'%p)



    
    
    