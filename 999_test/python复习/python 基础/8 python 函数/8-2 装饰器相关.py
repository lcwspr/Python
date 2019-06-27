"""
    注意  装饰器 的执行时间  是立即执行

"""


# 给发说说函数增加一些额外的功能
# 1 函数的名字不能发生改变
# 2 函数体内部的代码不能发生改变


def check(func):
    print("hello")

    def inner():
        print("登录验证操作。。。。。")
        func()
        # fss()
        # ftp()

    return inner


@check
def fss():
    print("发说说")


# fss = check(fss)

# fss()

# 当写@check时  装饰器  check() 函数就已经执行了  而不会等到函数调用在执行


"""
    装饰器   相关知识点 
        进阶 
            装饰器的叠加 
                    从上到下装饰
                    从下到上执行
                    
            对有参函数进行装饰
                    无论什么场景 保证函数调用参数个数一致
                    为了通用  可以使用不定长参数  结合  拆包操作  进行处理    
                                                                    
            对有返回值的函数进行装饰
            带有参数的装饰器
"""


def zhuangshiqi_line(func):
    def inner():
        print("-" * 40, end='')
        func()
    return inner

def zhuangshiqi_star(func):
    def inner():
        print("*" * 40, end='')
        func()
    return inner


@zhuangshiqi_star  #  print_hello() = zhuangshiqi_start(print_hello)
@zhuangshiqi_line  # print_hello() = zhuangshiqi_line(print_hello)
def print_hello():
    print("我是你爸爸,人狠话不多")

print_hello()









# 对有参函数进行装饰

def zsq(func):
    def inner():
        print("hello"*20)
        func()
    return inner

@zsq     # pnum = zsq(pnum)
def pnum():
    print(10)

pnum()

"""

 1 先开辟一个空间  存放zsq这个函数
 2 往下走  开辟空间 存放pnum这个函数
 3  执行pnum()  输出10
 
 
 加入装饰器 
 1 先开辟一个空间  存放zsq这个函数
 2 往下走  开辟空间 存放pnum这个函数
 3 将zsa中 func 指向qnum

"""
