# 闭包： 嵌套函数，内部函数调用外部函数的变量

def outer():
    a = 1
    def inner():
        print(a)

    print(inner.__closure__)
outer()


# 内部函数引用着外部函数的变量，那么如果外部函数返回内部函数，这个外部函数的执行环境将会一直被保留
def outer():
    a = 1
    def inner():
        nonlocal a
        a += 2
        print(a)
    return inner
outer()

f = outer()
f()
f()


# 闭包的用途
# import urllib   # url请求模块模块
from urllib.request import urlopen

def get_url():
    ret = urlopen('http://www.xiaohuar.com/index.html').read().encode('gbk')
    print(ret)

def get_url2():
    url = 'http://www.xiaohuar.com/index.html'
    def get():
        ret = urlopen(url).read().encode('gbk')
        print(ret)
    return get

get_func = get_url2()




