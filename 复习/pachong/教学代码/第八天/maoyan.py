#http://maoyan.com/cinemas
import urllib.request 
import urllib.parse
import ssl
import re
import pymysql

def main(page):
    #目标url
    # http://maoyan.com/cinemas
    # http://maoyan.com/cinemas?offset=12
    url = 'http://maoyan.com/cinemas?' + 'offset=' + str((page-1)*12)
    #获取网页数据，先构造一个请求
    request = urllib.request.Request(url)
    #发送请求，获取响应
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
        
    # print(html)
    with open('filename.html','w') as f:
        f.write(html)

    #以后遇到正则匹配出现问题的时候，首先检查正则表达式，如果确定正则表达式，没有问题
    #这时候可以把页面中的需要匹配的文本单独拿出来，再进行匹配，这个时候，复制出来的文本，
    #如果跟我们再网页上看到的不一样，那我们就需要将页面保存在本地，本地的html与网页显示的对比，找出问题
    #如果不一致，我们一本地的html文本写匹配规则
    # html1 = """
    # <div class="cinema-info">
    #     <a href="/cinema/15280?poi=99389254" class="cinema-name" data-act="cinema-name-click" data-bid="b_4tkpau4m" data-val="{city_id: 1, cinema_id: 15280}">青春光线电影院</a>
    #     <p class="cinema-address">地址：东城区滨河路乙1号雍和航星园74-76号楼</p>
    # </div>
    # """
    #目标数据（名称、地址、连接）
    pattern = re.compile('<a.*?href="(.*?)".*?cinema-name.*?>(.*?)</a>.*?cinema-address.*?>(.*?)</p>',re.S)
    result = re.findall(pattern,html) #返回的是一个list[]
    # print(result)
    #可以将不完整的电影院性情地址拼接完整urllib.parse.urljoin()
    # connect = pymysql.Connect(host = 'localhost',user='root',password='ljh123456',database='库名',port=3306,charset='utf-8')
    # cursor = connect.cursor()
    #"表名：movies"
    # insert_sql = """
    #     INSERT INTO movies(name,fullurl,adress) VALUES(%s,%s,%s)
    # """
    for i in result:
        # print(i)
        full_url = urllib.parse.urljoin(url,i[0])
        # print(full_url)
        name = i[1]
        adress = i[2]
        # cursor.execute(insert_sql,[name,full_url,adress])
        # connect.commit()
        # print(name,full_url,adress)
        

def main2(offset):
    url = 'http://maoyan.com/cinemas' + offset
    #获取网页数据，先构造一个请求
    request = urllib.request.Request(url)
    #发送请求，获取响应
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')

    #提取下一页的连接，需要一个正则表达式
    #<a class="page_19" href="?offset=216">下一页</a>
    # pattern = re.compile(r'<a.*?"page.*?".*?href=".*?".*?>下一页',re.S)
    # pattern = re.compile('>19</a>.*?<a.*?href="(.*?)".*?>下一页',re.S)
    pattern = re.compile('>19</a>.*?<a.*?href="(.*?)".*?>下一页</a>',re.S)
    next_page = re.findall(pattern,html) # 返回的是一个list
    print(next_page)
    if next_page:
        main2(next_page[0])
    
    #目标数据（名称、地址、连接）
    pattern = re.compile('<a.*?href="(.*?)".*?cinema-name.*?>(.*?)</a>.*?cinema-address.*?>(.*?)</p>',re.S)
    result = re.findall(pattern,html) #返回的是一个list[]
    # print(result)
    #可以将不完整的电影院性情地址拼接完整urllib.parse.urljoin()
    # connect = pymysql.Connect(host = 'localhost',user='root',password='ljh123456',database='库名',port=3306,charset='utf-8')
    # cursor = connect.cursor()
    #"表名：movies"
    # insert_sql = """
    #     INSERT INTO movies(name,fullurl,adress) VALUES(%s,%s,%s)
    # """
    for i in result:
        # print(i)
        full_url = urllib.parse.urljoin(url,i[0])
        # print(full_url)
        name = i[1]
        adress = i[2]
        # cursor.execute(insert_sql,[name,full_url,adress])
        # connect.commit()
        # print(name,full_url,adress)


if __name__ == '__main__':
    print('执行')
    # main(1)
    #方法一，for循环执行
    # for i in range(1,20):
    #     main(i)

    #方法二，直接找下一页
    main2('?offset=0')
   


