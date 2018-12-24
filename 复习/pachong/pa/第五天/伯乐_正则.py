# import urllib.request,urllib.parse



"""
 create table bole( id int auto_increment primary key, publishtime varchar(20), title varchar(100), type varchar(20) default null,  commentnum varchar(20) default null,  link varchar(100));

"""

from urllib.request import Request
import re
import pymysql
import urllib.request

def get_page_data(startpage, endpage, url):
    for i in range(startpage, endpage + 1):
        # 构建完整的目标URL
        fullurl = url + 'page/%s/' % i
        # 调用方法发起请求
        send_request(fullurl)
        print(fullurl)


def send_request(fullurl):
    print(fullurl + '正在下载')
    headers = {
         'User-Agent':'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146MobileSafari / 537.36',
     }
    req = Request(fullurl,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(fullurl + '下载完成')
    b = r'<!-- the loop -->.*? <!-- end of the loop -->'
    compile1 = re.compile(b, re.S)
    result1 = re.findall(compile1, html)
    a = r'<li.*?class="media">(.*?)</li>'
    compile2 = re.compile(a, re.S)
    result = re.findall(compile2, str(result1))
    c = r'.*?•.*?'
    d = r'<i\sclass="fa\sfa-comments-o"></i>'
    compile3 = re.compile(c, re.S)
    compile4 = re.compile(d, re.S)
    ff = []
    tf = []
    ft = []
    tt = []
    for i in result:

        res = re.findall(compile3, str(i))
        ret = re.findall(compile4,str(i))
        if len(res) == 0:
            if len(ret) == 0:
                ff.append(i)
               # print('没评论，没类型')
            else:
                tf.append(i)
                #print('有评论，没类型')
        else:
            if len(ret) == 0:
                ft.append(i)
               # print('没评论，有类型')
            else:
                tt.append(i)
               # print('有评论，有类型')
    FF = r'<a\starget="_blank"\shref="(.*?)">(.*?)</a><label.*?<span>(.*?)</span>'
    compile0= re.compile(FF, re.S)
    ffres = re.findall(compile0, str(ff))
    for info in ffres:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole VALUES(0,"%s","%s",0,0,"%s")'%(info[2],info[1],info[0])
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        conn.close()

    TF = r'<a\starget="_blank"\shref="(.*?)">(.*?)</a><label.*?<span>(.*?)</span>.*?</i>(.*?)</a>'
    compile0= re.compile(TF, re.S)
    tfres = re.findall(compile0, str(tf))

    for info in tfres:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole VALUES(0,"%s","%s",0,"%s","%s")'%(info[2],info[1],info[3],info[0])
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        conn.close()

    FT = r'<a\starget="_blank"\shref="(.*?)">(.*?)</a><label.*?<span>(.*?)</span>.*?•<span\sclass="p-tags"><a\shref=.*?>(.*?)</a>'
    compile0= re.compile(FT, re.S)
    ftres = re.findall(compile0, str(ft))
    for info in ftres:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole VALUES(0,"%s","%s","%s",0,"%s")'%(info[2],info[1],info[3],info[0])
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        conn.close()

    TT = r'<a\starget="_blank"\shref="(.*?)">(.*?)</a><label.*?<span>(.*?)</span>.*?•<span\sclass="p-tags"><a\shref=.*?>(.*?)</a>.*?</i>(.*?)</a>'
    compile0= re.compile(TT, re.S)
    ttres = re.findall(compile0, str(tt))
    for info in ttres:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='bole', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO bole VALUES(0,"%s","%s","%s","%s","%s")'%(info[2],info[1],info[3],info[4],info[0])
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        conn.close()



    with open('bole.html','w') as f:
        f.write(str(result))




if __name__ == '__main__':
    startpage = input('请输入开始页码（从1开始）：')
    endpage = input('请输入结束页码：')
    print(startpage, endpage)
    url = 'http://top.jobbole.com/'
    get_page_data(int(startpage), int(endpage), url)