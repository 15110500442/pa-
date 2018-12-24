import urllib.request as request
import urllib.parse as parse
#import ssl

#目标网址
url = 'http://www.1905.com/film/?fr=homepc_menu_news'
response = request.urlopen(url)
resultcontent = response.read().decode('utf-8')
print(response.read().decode('utf-8'))
with open('03.html','w') as f:
     f.write(resultcontent)