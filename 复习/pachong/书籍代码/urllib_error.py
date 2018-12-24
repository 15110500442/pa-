import urllib.error
import urllib.request
import socket
try:
    response1 = urllib.request.urlopen('http://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time OUT')
    