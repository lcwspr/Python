"""
    给发说说添加额外功能
        1 函数名字不能发生改变
        2 函数体内部的代码不能发生改变

"""

def check(func):
    print('hhhh')
    def inner():
        print("登录验证操作")
        func()
    return inner

@check
def fss():
    print('发说说')

# fss()

#  是调用fss() 时装饰器执行 还是写上@时装饰器执行那？
#  写上之后  就立即执行