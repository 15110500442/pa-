import time
import json
from lxml import etree
from selenium import webdriver


def dakai():
    browse = webdriver.Chrome(executable_path='/home/bc/下载/chromedriver')
    browse.get('https://www.taobao.com/')
    browse.find_element_by_id('q').send_keys('美食')
    time.sleep(2)
    browse.find_element_by_xpath('//div/button[@class="btn-search tb-bg"]').click()
    html = browse.page_source
    paqu(html, browse)


def paqu(html, browse):
    try:
        html = html
        response = etree.HTML(html)
        jieshou = response.xpath('//div[@class="item J_MouserOnverReq  "]')
        time.sleep(5)

        for i in jieshou:
            title = i.xpath('.//img[@class="J_ItemPic img"]/@alt')[0]
            pic = i.xpath('.//div[@class="pic"]/a/img/@src')[0]
            price = i.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()')[0]
            shangdian = i.xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]/text()')
            fukuan = i.xpath('.//div[@class="deal-cnt"]/text()')
            print(title, pic, price, shangdian, fukuan)
            dict = {
                '标题':title,
                '图片链接':pic,
                '价格':price,
                '商铺':shangdian,
                '付款人数':fukuan,
            }
            with open('taobao.json','a') as f:
                f.write(json.dumps(dict,ensure_ascii=False) + '\n')
        browse.find_element_by_xpath('//li[@class="item next"]/a[@class="J_Ajax num icon-tag"]').click()
        html = browse.page_source
        paqu(html, browse)
    except Exception as err:
        print(err)
        browse.close()


if __name__ == '__main__':
    dakai()
