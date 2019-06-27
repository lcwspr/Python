# 装饰器形成的过程
# 装饰器的作用
# 原则 ： 开放封闭原则
# 装饰器的固定模式


# 懂技术的公司
# bug

# 不懂技术的公司
# 代码量

import time

print(time.time()) # 获取当前时间
time.sleep(2)  # 让程序执行到这个位置的时候停一会
# print('hahahaha')

# test01
print('test01')
def func():
    start = time.time()
    print('老板好 同事好 大家好')
    time.sleep(0.01)
    end = time.time()
    return end - start
func()


# test02
print('test02')
def timmer(f):
    start = time.time()
    f()
    end = time.time()
    print(end - start)

def func():
    time.sleep(0.01)
    print('老板好 同事好 大家好')

timmer(func)


# test03
#  但还是要改动代码  要把所有的func改成 timer(func)
# 最终还是应该调用func
print('test03')

def func():
    time.sleep(0.01)
    print('老板好 同事好 大家好')


def timmer(f): # 装饰函数
    def inner():
        start = time.time()
        f()   # 被装饰的函数
        end = time.time()
        print(end - start)
    return inner

func = timmer(func)
func()



# test04
# 在不修改原来函数调用方式的前提下，还在原来函数的前后去添加功能
# timmer就是一个装饰器函数，只是对一个函数有一些装饰作用
# 通过闭包函数返回内部函数，来修改原函数，在外面再来接受他，和原来的名字保持一致

# 原则：  开放封闭原则
# 开放  ： 对拓展是开放的
# 封闭  ： 对修改是封闭的

# 封版
# 已经实现了一个功能，就不要修改一点点原代码。
