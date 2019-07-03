# 生成器  ---- 迭代器
    # 生成器函数   ---  本质就是我们自己写的函数
    # 生成器表达式

# 生成器函数
    # 只要函数yield关键字的函数都是生成器函数
    # yield不能和return共用,并且需要写在函数内部
def generator():
    print(1)
    yield 'a'
# 生成器函数： 执行之后会得到一个生成器作为返回值
ret = generator()  # 生成器本身就是一个迭代器
print(ret)
print(ret.__next__())

def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'
ret = generator()
print(ret)
print(ret.__next__())
print(ret.__next__())
# print(ret.__next__())     # 报错

# 我想要200个哇哈哈  带编号
def haha():
    for i in range(200000):
        yield '哇哈哈%s' % i
# for i in haha():
#     print(i)
g = haha()
count = 0
for i in g:
    count += 1
    print(i)
    if count > 50:
        break
print('我还能继续走  %s'%next(g))