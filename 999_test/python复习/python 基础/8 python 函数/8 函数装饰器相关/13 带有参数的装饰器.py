"""
    接受参数来简化代码

    通过@装饰器(参数)的方式 调用这个函数  并传递参数 并把返回值 再次当做装饰器来使用
    先计算@后面的内容  把这个内容当做是装饰器

"""

def getzsq(char):
    def zsq(func):
        def inner():
            print(char * 30)
            func()

        return inner
    return  zsq


def zsq(func):
    def inner():
        print("-"*30)
        func()
    return inner

def zsqe(func):
    def inner():
        print("="*30)
        func()
    return inner

def zsqs(func):
    def inner():
        print("*"*30)
        func()
    return inner


@getzsq('3')
def f1():
    print('6666')


f1()