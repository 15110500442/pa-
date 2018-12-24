#是以逗号分割
import csv

#csv 文件读入
with open('zhiwei.csv','a') as csvfile:
    #创建一个csv的文件操作句柄
    fieldnames = ['title','job_type','need_pople','adress','publish']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    #先写入头部信息
    writer.writeheader()
    #但行插入
    writer.writerow(dict)

#csv 文件读取
with open('data.csv','r') as csvfile:
    #读取csv文件
      lines = csv.reader(csvfile)
      for line in lines:
          print(line)