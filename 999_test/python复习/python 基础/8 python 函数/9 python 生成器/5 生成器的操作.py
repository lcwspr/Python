"""
    send() 方法
            send方法 有一个参数 指定的是上一次被挂起的yield语句的返回值
            相比于.__next__()     可以额外的给yield 语句传值
            注意第一次调用 t.send(None)


"""


def test():
    res = yield 1
    print(res)

    res2 = yield 2
    print(res2)

g = test()
print(g.send(None))
# print(g.__next__())


print(g.send("hello"))














