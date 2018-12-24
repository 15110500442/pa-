from lxml import etree
import re
import requests
from fake_useragent import UserAgent
import os


def main():
  ua = UserAgent()
  header = {
      'User-Agent':ua.chrome,
      #'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146Safari / 537.36',
      'Cookie':'_ga=GA1.2.2087541710.1514710342; remember_user_token=W1s5MTI4MDQ0XSwiJDJhJDExJEZZUlpVUkhnT293Q2FqZkk2NnQ2Y2UiLCIxNTI4MDcwMDE4LjI0MDI4NjgiXQ%3D%3D--2daae9f5e93e3ec0800fb17a47014309fd1a39a3; _m7e_session=16d2ca49ef2a925931e3327ae5416ba6; read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1527825114,1528069989,1529020501,1529023730; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%229128044%22%2C%22%24device_id%22%3A%22160abc59c9e57f-030172a8b0119a-71103742-1327104-160abc59c9f611%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22index-collections%22%7D%2C%22first_id%22%3A%22160abc59c9e57f-030172a8b0119a-71103742-1327104-160abc59c9f611%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1529023839',
      'X-CSRF-Token':'EDLvXBTXmzMb1/tg9zlQOksi36JOWSla9xZR3p9cPqh6o5OUkWhbvBO9gxJ603XoK7iv28AM5yOEvD5/s9YZtA=='}
  for i in range(1,3):
      url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=%s'%i
      response = requests.get(url,headers=header)
      html = etree.HTML(response.text)
      a = html.xpath('//div[@id="list-container"]/ul')
      for lianjie in a:
          title = lianjie.xpath('.//a[@class="title"]/text()')
          link = lianjie.xpath('.//a[@class="wrap-img"]/@href')
          for i in link:
            url1 = 'https://www.jianshu.com'+ str(i)
            response = requests.get(url1, headers=header)
            html = etree.HTML(response.text)
            b = html.xpath('//div[@class="note"]/div[@class="post"]')
            c =[]
            for i in b:
                title1 = i.xpath('.//h1[@class="title"]/text()')[0]
                time = i.xpath('.//span[@class="publish-time"]/text()')[0]
                content = i.xpath('.//div[@class="show-content-free"]//p/text()')
                tupain = i.xpath('.//div[@class="image-view"]/img/@data-original-src')
                file_path = 'jianshu/' + str(title1)[:4]
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                c.append(title1)
                # c.append(time)
                # c.append(content)
                # c.append(tupain)
                # filename = 'jianshu/'+str(title1)[:4]+'/'+title1+'.txt'
                # with open(filename,'a') as f:
                #    f.write(str(c))










if __name__ == '__main__':
    main()