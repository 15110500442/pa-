# post请求
#以拉钩网为例
import requests

# 目标url是一个post请求
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first':'false',
    'kd':'php',
    'pn':'1',
}
# Host: www.lagou.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0
# Accept: application/json, text/javascript, */*; q=0.01
# Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
# Accept-Encoding: gzip, deflate, br
# Referer: https://www.lagou.com/jobs/list_php?labelWords=&fromSearch=true&suginput=
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# X-Requested-With: XMLHttpRequest
# X-Anit-Forge-Token: None
# X-Anit-Forge-Code: 0
# Content-Length: 23
# Cookie: WEBTJ-ID=20180606101128-163d2dcfdc7a7-042e33f64da4138-4a5268-480000-163d2dcfdca330; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251088,1528251098,1528251106,1528251135; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251273; _ga=GA1.2.398997562.1528251089; user_trace_token=20180606101129-ec81d900-692e-11e8-9238-525400f775ce; LGSID=20180606101138-f1c4fb5b-692e-11e8-9238-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K600000-SwTdAzCGTxJTVclIBAA0Xgc8ZfPLqEBauB2swCkcXInK4sSxqCJzYLOkdwUryibfHPs-HSy_zACfeiIE56T0pmqzXYM8ZKVJj7yYPzqsruSCqIlAxAskU6LGPzGe-x3zbRXfKuRPYoB_XGLgwYRJYutcMPMh31Q758r_P5OS-6.7b_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzL4XNPIIhExzsq-LAS1-C_lMm7BmY8BCEBHzqMQIJyAp7WF_3vU-0.U1Yk0ZDqUA7MULR0TA-W5HD0Ijd_myIEIfKGUHYznjf0u1ddugK1n0KdpHdBmy-bIykV0ZKGujYk0APGujYs0AdY5HDsnHIxnH0krNtknjc1g1DsPjuxn1msnfKopHYs0ZFY5HbzP6K-pyfqnHf1P-tznH03P-tzPWf1n6KBpHYznjf0UynqP1nsnHfLPWbYg1Dsnj7xnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HT0UMfqn0K1XWY0IZN15HDzPWT3rjfdn1nknWf3rjcvrHRk0ZF-TgfqnHRzrjcdnH03n1Tkn0K1pyfqmHckuHwbrH6snj0snjfYm6KWTvYqPbDvrHbzPH9Af16dfWIar0K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1nHb4nWKxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1Ydn103Pf%26ck%3D1962.1.92.280.309.280.301.496%26shh%3Dwww.baidu.com%26sht%3Dmonline_4_dg%26us%3D1.0.2.0.2.1194.0%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_4_dg%26wd%3Dlagou%2520%26oq%3Dlagou%26rqlang%3Dcn%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_bj_e110f9_c4d3b0_lagou; LGRID=20180606101228-0fbeae75-692f-11e8-9238-525400f775ce; LGUID=20180606101129-ec81dc13-692e-11e8-9238-525400f775ce; _gid=GA1.2.261770398.1528251090; JSESSIONID=ABAAABAAAGFABEF0D3C8A904F64AC7C24974B45BB8F6CFE; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; SEARCH_ID=176033aa1a21423d8b0302c81bbfe2e1
# Connection: keep-alive

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    'cookie':'WEBTJ-ID=20180606101128-163d2dcfdc7a7-042e33f64da4138-4a5268-480000-163d2dcfdca330; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251088,1528251098,1528251106,1528251135; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528251273; _ga=GA1.2.398997562.1528251089; user_trace_token=20180606101129-ec81d900-692e-11e8-9238-525400f775ce; LGSID=20180606101138-f1c4fb5b-692e-11e8-9238-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K600000-SwTdAzCGTxJTVclIBAA0Xgc8ZfPLqEBauB2swCkcXInK4sSxqCJzYLOkdwUryibfHPs-HSy_zACfeiIE56T0pmqzXYM8ZKVJj7yYPzqsruSCqIlAxAskU6LGPzGe-x3zbRXfKuRPYoB_XGLgwYRJYutcMPMh31Q758r_P5OS-6.7b_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzL4XNPIIhExzsq-LAS1-C_lMm7BmY8BCEBHzqMQIJyAp7WF_3vU-0.U1Yk0ZDqUA7MULR0TA-W5HD0Ijd_myIEIfKGUHYznjf0u1ddugK1n0KdpHdBmy-bIykV0ZKGujYk0APGujYs0AdY5HDsnHIxnH0krNtknjc1g1DsPjuxn1msnfKopHYs0ZFY5HbzP6K-pyfqnHf1P-tznH03P-tzPWf1n6KBpHYznjf0UynqP1nsnHfLPWbYg1Dsnj7xnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HT0UMfqn0K1XWY0IZN15HDzPWT3rjfdn1nknWf3rjcvrHRk0ZF-TgfqnHRzrjcdnH03n1Tkn0K1pyfqmHckuHwbrH6snj0snjfYm6KWTvYqPbDvrHbzPH9Af16dfWIar0K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1nHb4nWKxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1Ydn103Pf%26ck%3D1962.1.92.280.309.280.301.496%26shh%3Dwww.baidu.com%26sht%3Dmonline_4_dg%26us%3D1.0.2.0.2.1194.0%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_4_dg%26wd%3Dlagou%2520%26oq%3Dlagou%26rqlang%3Dcn%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_bj_e110f9_c4d3b0_lagou; LGRID=20180606101228-0fbeae75-692f-11e8-9238-525400f775ce; LGUID=20180606101129-ec81dc13-692e-11e8-9238-525400f775ce; _gid=GA1.2.261770398.1528251090; JSESSIONID=ABAAABAAAGFABEF0D3C8A904F64AC7C24974B45BB8F6CFE; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; SEARCH_ID=176033aa1a21423d8b0302c81bbfe2e1',
    'Referer':'https://www.lagou.com/jobs/list_php?labelWords=&fromSearch=true&suginput=',
    'Host':'www.lagou.com',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}

response = requests.post(url,data=data,headers=header)
# print(response.text)
print(response.status_code)
#使用json()可以直接将一个json字符串转换为python的对象一般要么是字典，要么是list(数组)
data = response.json()
print(data['content']['hrInfoMap']['2305269'])
print(type(data))

