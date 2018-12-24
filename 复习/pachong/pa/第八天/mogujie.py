import re
import csv
import urllib.request
import urllib.parse
import requests
import json
def urls(url):
    headers = {
        'User - Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.84Safari / 537.36',
        'Cookie':'__mgjuuid=c57eb663-12dd-4da1-9e75-e93dedcec5fb; _ga=GA1.2.1017568902.1528418742; _gid=GA1.2.1249798311.1528418742; _mwp_h5_token_enc=e9c9b063713929bece40ac33f3564550; _mwp_h5_token=f506a6f09bb775a5fa335a4fd44aa38f_1528437539366',
    }
    req = urllib.request.Request(url,headers=headers)
    print(req)
    return req
def response():
    menuList = []
    typDict = {}
    MoguUrl = 'http://www.mogujie.com/'
    data = {
        'ptp':'1.fqjWab.0.0.do91q9A4'
    }
    response = requests.get(MoguUrl)
    result = response.text
    a = r'class="pc_i.*?(\d*?)">'
    ret = re.compile(a,re.S)
    menuResult = re.findall(ret,result)
    menuUrl = 'http://mce.mogucdn.com/jsonp/multiget/3?pids=%s'%menuResult[0]
    print(menuUrl)
    menuResponse = requests.get(menuUrl)
    menuText = menuResponse.text
    menuText = menuText.replace('null(','').replace(')','')
    menu = json.loads(menuText)
    for i in menu['data']['110119']['list']:
        menuList.append(i['categoryPid'])
    menuStr = '%2C'.join(menuList)
    typeUrl = 'http://mce.mogucdn.com/jsonp/multiget/3?pids=%s'%menuStr
    print(typeUrl)
    typeResponse = requests.get(typeUrl)
    typeText = typeResponse.text
    typeText = typeText.replace('null(','').replace(')','')
    typ = json.loads(typeText)
    for inde in menuList:
        for i in typ['data'][str(inde)]['list']:
            name = i['title']
            link = i['link']
            typDict[name] = link
    print(typDict.keys())
    want = input('输入查找的商品类型')
    print(typDict[want])
    cid = r'http://list.mogujie.com/.*?/(\d*?){5}.acm='
    cids = re.compile(cid,re.S)
    cid = re.findall(cids,str(typDict[want]))
    start = int(input('请输入起始页'))
    end = int(input('请输入起始页'))
    p = 0
    for foo in range(start,end+1):
        wantUrl = 'http://list.mogujie.com/search?cKey=15&page=%s&sort=pop&ad=0&fcid=%s'%(foo,cid[0])
        print(wantUrl)
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
if __name__ == '__main__':
    response()
