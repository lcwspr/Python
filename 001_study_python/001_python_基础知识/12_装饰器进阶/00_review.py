# 复习
# 将作业
# 装饰器进阶
    # functools.wraps
    # 但参数的装饰器
    # 多个装饰器装饰同一个函数

# 周末的作业
    # 文件操作
    # 字符串处理
    # 输入输出
    # 流程控制


# 装饰器
# 开发原则：  开放封闭原则
# 装饰器的作用： 在不改变原函数的调用方式的情况下，在函数的前后添加功能
# 装饰器的本质： 闭包函数

# test01
print('\ntest01')
def wrapper(func):
    def inner(*args, **kwargs):
        print('''函数前添加功能''')
        ret = func(*args, **kwargs)
        print('''函数后添加功能''')
        return ret
    return inner

@wrapper        # holiday = wrapper(holiday)
def holiday(day):
    print('全体放假%s天' % day)
    return '好开心'

ret = holiday(2)
print(ret)


# test02
print('\ntest02')
def outer(*args, **kwargs):
    print(args)
    print(*args)

outer(1, 2, 3, 4)   #  == outer(*[1,2,3,4])   #  == outer(*(1, 2, 3, 4))




































