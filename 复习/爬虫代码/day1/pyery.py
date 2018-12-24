from pyquery import PyQuery
import lxml
import requests


url = 'http://blog.jobbole.com/all-posts/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
response = requests.get(url,headers=header)
with open('bolezaixian.html','a') as f:
    f.write(response.text)
pq_html = PyQuery(response.text)
print(pq_html)
