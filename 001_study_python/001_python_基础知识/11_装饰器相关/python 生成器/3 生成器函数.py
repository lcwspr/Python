"""
    生成器函数
        函数中包含yield语句
        这个函数的执行结果就是“生成器”


    yield 可以去阻断当前的函数执行 然后 当使用next()函数 或者 __next__()  都会让这个函数继续执行
    当执行到下一个yield就又会被暂停


"""
def test():
    print("xxx")
    yield 1
    print(1)

    yield 2
    print(2)

    yield 3
    print(3)

    yield 4
    print(4)

    yield 5
    print(5)


g = test()
print(g)

print(g.__next__())
print(g.__next__())
# print(g.__next__())
# print(g.__next__())





































