from bs4 import BeautifulSoup
import requests
import pymysql
import json
import re

url = 'https://www.autohome.com.cn/all/1/'
header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36'

}
response = requests.get(url,headers = header)
print(response.status_code)
with open('qi.html','w') as f:
    f.write(response.text)
html = response.text
soup = BeautifulSoup(response.text,features='html.parser')
#获取的数据（图片连接、标题、时间、观看量、评论量、完整文章详情连接、简介内容）保存数据库，
#注意使用beautifulsoup的css选择器获取数据，保证数据库内容不重复
a = soup.select('.article li')
objids = []
# print(len(a))
# hh = soup.find_all('h3')
# print(hh)
#获取属性有两种：get("属性名字") 和 attrs[’属性名‘]
for i in a:
    link = i.select('a')
    if len(link) != 0:
        link = i.select('a')[0].attrs['href']
        tupian = i.select('img')[0].attrs['src']
        title = i.select('h3')[0].get_text()
        time = i.select('.fn-left')[0].get_text()
        guankan = i.select('em')[0].get_text()
        comment = i.select('em')[1].get_text()
        jianjie = i.select('p')[0].get_text()
        #从文章的详情url中获取ip
        # b = re.compile(r'.*?cn.*?/\d*?/(.*?)[-,.].*?.html')
        # id = re.findall(b,link)
        # objid.append(id)
        # print(objids)
        #print(link,tupian,title,time,guankan,comment,jianjie)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='qiche', port=3306,charset='utf8')                     
    cur = conn.cursor()
    sql = 'INSERT INTO qiche(link,tupian,title,time,guankan,comment,jianjie) VALUES("%s","%s","%s","%s","%s","%s","%s")'
    cur.execute(sql,(link,tupian,title,time,guankan,comment,jianjie))
    result = cur.fetchall()
    conn.commit()
    conn.close()
    #https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?
    #appid=1&dateType=jsonp&
    #objids=918300.918298.918297.918173.918296.918172.918293.918193.918123.918174.918285.918290.918286.918265.918234&callback=jQuery172015815106084248387_1528424393377&_=1528424393675