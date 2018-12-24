# lxml_test.py

# 使用 lxml 的 etree 库
from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<a>
    <li class="item-1"><a href="link2.html">second item</a></li>
</a>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
</ul>
</div>
'''
# / 是从根目录开始
# //  是不考虑位置
# 转换成html文本类型
a = etree.HTML(text)
# print(a)
# 转换成字符串类型
# 如果要读取本地的HTML可以使用下面的方法
# b = etree.parse('本地文件')
result = etree.tostring(a)
# print(result)

c = a.xpath('//div/ul//li[1]')
print(c)
