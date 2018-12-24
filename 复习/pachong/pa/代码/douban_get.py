import urllib.parse as parse

url = 'https://www.baidu.com/s?ie=utf-8'
a = parse.urlparse(url)
print(a)
#ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='ie=utf-8', fragment='')
