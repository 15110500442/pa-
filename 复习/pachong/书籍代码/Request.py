import urllib.request

#使用Request请求
request = urllib.request.Request('https://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

#以下是Request可以传的参数
#def __init__(self, url, data=None, headers={},origin_req_host=None, unverifiable=False,method=None):


# html1 = re.compile(r'.*?<div.*?class="terminalpage-main clearfix".*?<ul.*?class="tab-ul".*?<li.*?class="current">(.*?)</li>'
#                    r'.*?<div.*?class="tab-inner-cont".*?<p>.*?<span>(.*?)</span>.*?</div>',re.S)
# b = re.findall(html1, text)
# print(b)
# html = etree.HTML(text)
# for i in html:
#     #//*[@id="clone_category"]/div[1]/div[1]/h1
#     title = i.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')
#     #公司名字
#     company_name = i.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()')
#     #会员图标
#     tupiao = i.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/img/@src')
#     #工作要求
#     gzyq1 = i.xpath('/html/body/div[6]/div[1]/ul//li/span/text()')
#     #工作要求详情
#     gzyq2 = i.xpath('/html/body/div[6]/div[1]/ul//li/strong/text()')
#     #发布时间
#     time = i.xpath('//*[@id="span4freshdate"]/text()')
#     #职位描述
#     zhiwei = i.xpath('/html/body/div[6]/div[1]/div[1]/div/div[1]//p/text()')
#     #职位描述详情
#     zhiwei1 = i.xpath('/html/body/div[6]/div[1]/div[1]/div/div[1]//p/span/text()')
#     zhiwei.extend(zhiwei1)
#     print(zhiwei)
