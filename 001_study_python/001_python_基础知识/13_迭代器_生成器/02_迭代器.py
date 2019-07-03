# 迭代器
# 注意：迭代器，装饰器 完全没有关系
print('test01')
l = [1, 2, 3]
for i in enumerate(l):
    print(i)
# 如何从列表中取值？
    # 索引
    # 循环 for     怎么循环拿出来的？
# 可以被for循环的东西
    # list
    # dic
    # str
    # set
    # tuple
    # f = open()
    # range()
    # enumerate()

print('\ntest02')
print(dir([])) # 告知一个数据类型拥有的所有方法
print(dir(3))
print(dir({}))
print(dir(''))
print(dir(range(10)))
print(set(dir([])) & set(dir({})) & set(dir('')) & set(dir(range(10))))  # 都有的属性

print('\ntest03')

# 一般管双下划线的方法叫做双下方法
    # 已经写好的C语言代码，能够通过不只一种方式调用他
print([1].__add__([2]))
print([1] + [2])
# 这就是语法，其实程序只认识代码不认识符号
s = 1
t = 2
print(s.__add__(t))  # python 解释器作用的事情

print('\ntest04')
# iterable 可迭代    __iter__
print('__iter__' in dir(int))
print('__iter__' in dir(bool))
print('__iter__' in dir(list))
print('__iter__' in dir(dict))
print('__iter__' in dir(set))
print('__iter__' in dir(tuple))
print('__iter__' in dir(enumerate([])))
print('__iter__' in dir(range(1)))

# 只要是能被for循环的数据类型, 就一定拥有__iter__方法
print([].__iter__())
# 一个列表执行了  __iter__() 【可以通过iter()函数调用】之后的返回值就是一个迭代器  iterator

# 迭代器对象比原可迭代对象多的就是和迭代相关的
print('\ntest05 ')
print(dir([]))
print(dir([].__iter__()))
print(set(dir([].__iter__())) - set(dir([])))

print([1, 2, 3].__iter__().__length_hint__())  # 就是可迭代对象的元素个数
#  __setstate__ 用于指定从哪一个位置开始取

print('\ntest06')
l = [1, 2, 4, 5]
iterator = l.__iter__()
print(iterator.__next__())   # 1
print(iterator.__next__())   # 2
print(iterator.__next__())   # 3
print(iterator.__next__())   # 5
# print(iterator.__next__()) # 报错

# Iterable  可迭代的     --> __iter__()   # 只要含有__iter__方法的都是可迭代的
# [].__iter__() 迭代器   --> __next__()   # 通过next就可以从迭代器中一个一个的取值

# 只要含有__iter__方法的都是可迭代的------可迭代协议(含有__iter__方法就可以被for循环操作，就是可迭代的)
# 迭代器协议 -- 内部含有__next__ 和 __iter__方法的就是迭代器
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance([],Iterable))


print('\ntest07')
class A:
    def __iter__(self):
        pass
    def __next__(self):
        pass
a = A()

print(isinstance(a,Iterator))
print(isinstance(a,Iterable))

print('\ntest08')
l = [1, 2, 3, 4]
l = l.__iter__()
l.__next__()
for i in l:
    print(i)


# 迭代器的概念
# 只要内部含有__next__和__iter__方法的就是迭代器

# 迭代器协议和可迭代协议
# 可以被for循环的都是可迭代的
# 可迭代的内部都含有__iter__()方法  (迭代器一定可迭代)
# 可迭代对象调用__iter__()方法就可以得到迭代器
# 迭代器中的__next__()方法可以一个一个的获取值

# 用途 ---- 想用for循环，而之后可迭代对象才能够使用for循环(), 当遇到一个新的变量不确定时候能时候for循环的时候，就判断他是否可迭代。
    # iterator
    # 可迭代对象
    # 直接给内存地址
print([].__iter__())


# for循环原理
# 1. 取得可迭代对象的迭代器对象
# 2. 调用next方法取值
# 3. 循环取值直到报错，自动处理错误

# 迭代器的好处
    # 从容器类型中一个一个的取值，会把所有的值都取到
    # 节省内存空间
        # range
        # f  open()
        # 迭代器并不会在内存中在占用一大块内存，而是随着循环每次生成一个
print('\ntest09')
print(range(1000000000))
print(list(range(10000000)))

print('\ntest10')
# 迭代器很好，但我们现在不想让他生成数字了，想生成2000000个字符串？

def func():
    for i in range(2000000):
        'wwwwaaa %s '% i
    # 怎么返回值？
    # 如果添加到列表中，相当于一下全放到内存中了，不需要迭代器了

# 生成器
# 迭代器特别好，但是不能满足需求，我们需要生成大量数据，但是不想让他在内存中一次性生成，还需要处处使用
# 自己写的迭代器，生成器

# 生成器函数   --- 本质就是我们自己写的函数
# 生成器表达式
