def test():
    for i in range(0, 10):
        yield i

f = test()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


"""
    产生数据的方式
            生成器具备可迭代特性 
            next() 函数  等价于  生成器.__next__()
            for in


"""