#urllib.error的容错
import urllib.error
import urllib.request
import ssl
req = urllib.request.Request('http://www.nkjcdsbckjbdbkc.com/')
context = ssl._create_unverified_context()

#最优方案：URLError是HTTPError父类
try: 
    response = urllib.request.urlopen(req,context=context,timeout=0.1)
    print('成功')
except urllib.error.HTTPError as err:
    print(err.code)
    print(err.reason)
except urllib.error.URLError as err:
    print('原因:'+ err.reason)
# except:
#     print('请求成功')
    

