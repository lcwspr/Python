# 带参数的装饰器
# 500个函数
# 增加了一层函数  为了能够接受出来外界传递给我的参数

print('test01')
import time
def get_timmer(flag = False):
    def timmer(func):
        def inner(*args,**kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs )
                end = time.time()
                print(end - start)
                return ret
            else:
                ret = func(*args, **kwargs )
                return ret
        return inner
    return timmer

# timer = get_time()
# @timer
@get_timmer(True)
def haha():
    time.sleep(0.01)
    print('i am haha')

@get_timmer()
def hehe():
    time.sleep(0.01)
    print('i am hehe')


haha()
hehe()


# 多个装饰器装饰一个函数
print('\ntest02')
def wrapper1(func):
    def inner1():
        print('wrapper1, before func')
        func()
        print('wrapper1, after func')
    return inner1

def wrapper2(func):
    def inner2():
        print('wrapper2, before func')
        func()
        print('wrapper2, before func')
    return inner2


# 套着执行的
# 从上到下解释，从下到上装饰
@wrapper2    # f = wrapper2(f) -->  wrapper2(inner1)  = inner2
@wrapper1    # f = wrapper1(f) = inner1
def f():
    print('in function')


f()          # inner2

# 记录用户的登录情况，
# 计算这个函数的执行时间