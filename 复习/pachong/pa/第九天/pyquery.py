from pyquery import PyQuery
import lxml
url = 'http://blog.jobbole.com/all-posts/'
pq_html = PyQuery(url)
print(pq_html)

