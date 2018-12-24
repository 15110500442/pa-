# post请求
# 以拉钩网为例
import requests

#  目标url：https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first': 'false',
    'pn': '2',
    'kd': 'python爬虫',
}

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36',
    'Cookie':'user_trace_token=20180501202657-adaf00f6-2663-4715-bfe0-ba4231090c65; _ga=GA1.2.7497763.1525177613; LGUID=20180501202659-f19f9759-4d3a-11e8-bb2f-5254005c3644;WEBTJ-ID=20180606101133-163d2dd12974c2-09c1b2967ba648-3a61430c-1327104-163d2dd1298670; _gid=GA1.2.1249805153.1528251094; JSESSIONID=ABAAABAAADEAAFI7EF3103B7C5DCA1CD4F83FA64A7AFAB9; LGSID=20180606101209-047482d2-692f-11e8-9238-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251094,1528251113,1528252690; SEARCH_ID=ae9e4501b5fb485aa47c8b7897fe2c8c; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528252808; LGRID=20180606104024-f6e2e1d9-6932-11e8-9241-525400f775ce',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=python',
}
a = requests.post(url, data=data, headers=header)
#print(a.status_code)
#print(a.text)
#使用json（）
#使用json（）可以直接将一个json的字符串转换为python的对象   一般要么是字典，要么是list（数组）
data = a.json()
print(data['content']['hrInfoMap']['4002110'])
print(type(data))