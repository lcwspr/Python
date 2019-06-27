# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
print('test01')

FLAG = False
def login(func):
    def inner(*args, **kwargs):
        global FLAG
        '''登录程序'''
        if FLAG:
            ret = func(*args, **kwargs)   # func是被装饰的函数
            return ret
        else:
            print('请输入用户名和密码')
            username = input('username : ')
            password = input('password : ')
            if username == 'boss_gold' and password == '22222':
                FLAG = True
                ret = func(*args, **kwargs)   # func是被装饰的函数
                return ret
            else:
                print('登录失败')
    return inner


@login
def shoplist_add():
    print('增加一件物品')

@login
def shoplist_del():
    print('删除一件商品')

# shoplist_add()
# shoplist_del()


# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
import time
print('\ntest02')

def logFunc(func):
    def inner(*args, **kwargs):

        ret = func(*args, **kwargs)
        with open('file/first.log',mode='a', encoding='utf-8') as f:
            f.write("时间 %f , 当前的调用为 %s\n"%(time.time(),func.__name__))
            f.close()
        return ret
    return inner

@logFunc
def myFirstFunc(a, b):
    print('我想要一个新奇的东西，啊哈哈哈哈  ', a , b)
    return 'good'

@logFunc
def mySecondFunc(c):
    print('我不想要东西 呵呵  ', c)
    return 'bad'

# myFirstFunc(12, 34)
# myFirstFunc(45, 84)
# mySecondFunc(35)
# mySecondFunc(53)
# myFirstFunc(73, 93)
# mySecondFunc(743)
# mySecondFunc(743)
# mySecondFunc(743)
# myFirstFunc(83, 47)

# 进阶作业(选做)：
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

from urllib.request import urlopen

import os
def cache(func):

    def inner(*args, **kwargs):

        if not os.path.exists('file/cache.txt'):
            with open('file/cache.txt',mode='wb') as f:
                f.write(b'')
        if os.path.getsize('file/cache.txt'):
            with open('file/cache.txt',mode='rb') as f:
                return f.read()
        else:
            ret = func(*args, **kwargs)
            with open('file/cache.txt',mode='wb') as f:
                f.write(b'*********' + ret)
        return ret
    return inner

@cache
def getPage(url):
    return urlopen(url).read()


print(getPage('https://www.baidu.com'))
print(getPage('https://www.baidu.com'))
print(getPage('https://www.baidu.com'))