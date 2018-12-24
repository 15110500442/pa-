from selenium import webdriver
from lxml import etree
import time
import json
import re
from selenium.webdriver.common.keys import Keys
def jidian():

    browse = webdriver.Chrome(executable_path='/home/bc/下载/chromedriver')
    browse.get('https://www.zhaopin.com/')
    browse.find_element_by_id('KeyWord_kw2').send_keys('技术')
    browse.find_element_by_class_name('doSearch').click()
    browse.find_element_by_class_name('pagesnum').send_keys(1)
    browse.find_element_by_xpath('//div[@class="pagesDown"]/ul/li[@class="pagesDown-pos"]/a').click()
    html = browse.page_source
    paqu(html, browse)
def paqu(html, browse):
    try:
        html = html
        #response = etree.HTML(html)
        response = re.compile('<tr.*?<td.*?class="zwmc".*?<a.*?>(.*?)</a>',re.S)
        a = re.findall(response,html)
        for i in a:
            title = i.replace('<b>','').replace('\n','').replace('</b>','')
            dict = {
                 '标题': title,
             }
            with open('zhilian.json', 'a') as f:
                 f.write(json.dumps(dict, ensure_ascii=False) + '\n')
        time.sleep(5)
        browse.find_element_by_class_name('pagesnum').send_keys(1)
        browse.find_element_by_xpath('//div[@class="pagesDown"]/ul/li[@class="pagesDown-pos"]/a').click()
        html = browse.page_source
        paqu(html, browse)
    except Exception as err:
        print(err)
        browse.close()
    #


if __name__ == '__main__':
    jidian()