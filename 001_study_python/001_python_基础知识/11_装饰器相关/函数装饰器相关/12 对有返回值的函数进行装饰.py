# 无论什么场景  保证返回值一致


# 返回值返回的是 内部函数func()  函数的执行  结果  返回就好

def zsq2(func):
    def inner(*args, **kwargs):
        print("_"*30)
        print(args, kwargs)
        val = func(*args, **kwargs)
        return val
    return inner



@zsq2
def pnum(num, num2, num3):
    print(num, num2, num3)
    return num + num2 + num3

@zsq2
def pnum2(num):
    print(num)


val1 = pnum(124, 233, num3 = 345)
val2 = pnum2(333)

print(val1, val2)




























