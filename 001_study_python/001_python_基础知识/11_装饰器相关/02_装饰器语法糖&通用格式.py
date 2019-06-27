import time

print('\ntest01')
def timmer(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('花费的时间为%f'%(end - start))
    return inner

@timmer
def myFunc():
    print('大家好 才是真的好')
    time.sleep(0.01)

# myFunc = timer(myFunc)

myFunc()

# 语法糖
# @装饰器函数名

print('\ntest02')
# test02
# 如果被装饰函数有返回值怎么办
def timmer02(f):
    def inner():
        start = time.time()
        ret = f()
        end = time.time()
        print('花费的时间为%f'%(end - start))
        return ret
    return inner

@timmer02
def myFunc02():
    print('大家好 才是真的好')
    time.sleep(0.01)
    return 'hello everybody'

print(myFunc02())


# test03
print('\ntest03')
# 如果被装饰函数有参数怎么办   # 装饰带参数函数的装饰器
def timmer03(f):
    def inner(a):
        start = time.time()
        ret = f(a)
        end = time.time()
        print('花费的时间为 %f'%(end - start))
        return ret
    return inner

@timmer03
def myFunc03(a):
    print('大家好 才是真的好 ' + str(a))
    time.sleep(0.01)
    return 'hello everybody'

print(myFunc03(20))

print('\ntest04')
# 装饰几个参数个数不同的函数的装饰器   其实有错误，不能接受关键字参数

def timmer04(f):
    def inner(*args):
        start = time.time()
        ret = f(*args)
        end = time.time()
        print('花费的时间为 %f'%(end - start))
        return ret
    return inner

@timmer04
def myFunc04_01(a):
    print('大家好 才是真的好 ' + str(a))
    time.sleep(0.01)
    return 'hello everybody'


@timmer04
def myFunc04_02(a, b):
    print('大家好 才是真的好 ' + str('%d, %d'%(a, b)))
    time.sleep(0.01)
    return 'hello everybody'

myFunc04_01(24)
myFunc04_02(12, 45)


print('\ntest04')
# 装饰几个参数个数不同的函数的装饰器   其实有错误，不能接受关键字参数

def timmer05(f):
    def inner(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        print('花费的时间为 %f'%(end - start))
        return ret
    return inner

@timmer05
def myFunc05_01(a):
    print('大家好 才是真的好 ' + str(a))
    time.sleep(0.01)
    return 'hello everybody'


@timmer05
def myFunc05_02(a, b):
    print('大家好 才是真的好 ' + str('%d, %d'%(a, b)))
    time.sleep(0.01)
    return 'hello everybody'

myFunc05_01(24)
myFunc05_02(12, b = 45)

# 装饰器的形成过程：
# 最简单的装饰器->有返回值的->有一个参数的->万能参数的
# wrapper  装饰器

# finish
print('\nfinish')
def wrapper(f):  # 装饰器函数,f是被装饰的函数
    def inner(*args, **kwargs):
        '''在被装饰函数之前要做的事'''
        ret = f(*args, **kwargs)  # 被装饰的函数
        '''在被装饰函数之后要做的事'''
        return ret
    return inner

@wrapper          # 语法糖 @装饰器函数名
def func(a, b):   # 被装饰的函数
    time.sleep(0.01)
    print('ahahaha  我成功了')
    return 'hello world'
