"""
    改6

    1 代码冗余问题
        定义函数接收一个函数

        def checkLogin(func):
            print("登录验证。。。。")
            func()

    2 但是业务逻辑代码需要被改变  还能够怎么修改？
    一个需求  保证业务逻辑代码不改变

        能不能重写该函数  fss  ftp

        就是相当于
        def checkLogin(func)
            print(...)
            func()
        def fss()
            print("发说说")

        fss = checkLogin(func)   行不行   不行

        运用闭包 将其变成一个拥有此函数体的函数



"""


def checklogin(func):
    def inner():
        print("登录验证")
        func()

    return inner


def fss():
    print("发说说")


@checklogin  # 语法糖功能
def ftp():
    print("发图片")


fss = checklogin(fss)
ftp = checklogin(ftp)

# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    # checkLogin(fss)
    fss()
else:
    # checkLogin(ftp)
    ftp()

# 利用闭包的特性   在函数原本的基础之上装饰了一些额外的小功能
# checklogin 被称为装饰器      这种操作被称为装饰器设计模式
