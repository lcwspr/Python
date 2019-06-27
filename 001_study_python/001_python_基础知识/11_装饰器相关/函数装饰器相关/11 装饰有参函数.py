#   直接编译  inner需要0个参数  但是你硬传了一个  我们执行的其实就是inner
#   装饰器问题



def zsq(func):
    def inner():
        print("_"*30)
        func()
    return inner

def zsq2(func):
    def inner(*args, **kwargs):
        print("_"*30)
        print(args, kwargs)
        func(*args, **kwargs)
    return inner


    #  可以运行  但是这个装饰器不通用  怎样构建一个通用的装饰器那？
    #
    # def zsq(func):
    # def inner(n):
    #     print("_"*30)
    #     func(n)
    # return inner


@zsq2
def pnum(num, num2, num3):
    print(num, num2, num3)



pnum(124, 233, num3 = 345)