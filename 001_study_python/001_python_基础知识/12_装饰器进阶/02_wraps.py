from functools import wraps


print('test01')

def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('装饰前的事情')
        ret = func(*args, **kwargs)
        print('在被装饰函数之后做的事')
        return ret
    return inner

@wrapper
def holiday(day):
    '''
    放假通知
    :param day:
    :return:
    '''
    print('全体放假%d天'%day)
    return 'happy'

print(holiday.__name__)   # 装饰完成之后，其实原函数已经变成了内部函数inner
# 可以使用一个方法让被装饰函数能够在外部正常的去使用他的方法

print('这样就正常了')
print(holiday.__doc__)


# test02
print('\ntest02')
def haha():
    '''
    一个打印haha的函数
    :return: 
    '''
    print('哇哈哈')

print('my name is ' + haha.__name__)
print(haha.__doc__)


















