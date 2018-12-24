from bs4 import BeautifulSoup
import requests

url = 'https://hr.tencent.com/position.php?&start=0#a'
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
}

response = requests.get(url,headers=header)
print(response.status_code)

with open('qche.html','w') as f:
    f.write(response.text)
html = response.text

soup = BeautifulSoup(open('qche.html'),'lxml')
# print(soup.prettify())
# print(type(soup))
li_result = soup.find_all('tr')
li_result1 = soup.find_all(class_='even')
li_result2 = soup.find_all(class_='odd')
for tr in li_result1:
    title = tr.select('td a')[0].get_text()
    typeq = tr.select('td')[1].get_text()
    pople = tr.select('td')[2].get_text()
    addr = tr.select('td')[3].get_text()
    print(title)
    print(typeq)
    print(pople)
    print(addr)

