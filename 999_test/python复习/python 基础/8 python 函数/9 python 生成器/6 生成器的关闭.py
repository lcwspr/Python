def test():
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")

    yield 4
    print("d")


g = test()
print(g.__next__())
print(g.__next__())
g.close()
print(g.__next__())
print(g.__next__())

#  关闭相当于把整个生成器的指针指向最后一个
