import os,sys
#程序的执行模块
from scrapy.cmdline import execute

# 这里表示指明项目的绝对路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy','crawl','zhilianzp'])