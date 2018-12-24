# 1、在函数外边定义的变量叫做全局变量 
# 2、全局变量能够在所有的函数中进行访问 
# 4、如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错 
# 5、如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，强龙不压地头蛇

_name = '苍老师'

def get_name():
    global _name
    _name = '泽马老师'
    print(_name)

def get_name1():
    global _name
    print(_name)


get_name()
get_name1()

