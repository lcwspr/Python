"""
    注意
        如果碰到return 语句
            会直接终止  抛出StopIteration 异常提示


            生成器只会遍历一次

"""

def test():
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")

    return 10


g = test()

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

print("-"*30)
for i in g:
    print(i)
print("-"*30)