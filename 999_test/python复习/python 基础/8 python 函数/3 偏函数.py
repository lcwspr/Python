"""

    概念 &  场景
        当我们写一个参数比较多的函数时，如果有些参数 大部分场景下都是某一个固定值，那么为了简化使用  就可以创建一个新的函数  指定我们要使用的函数的某个参数 为某个固定值  这个新函数就是偏函数


        import functools
        new func = functools.partial(test, c=5)

        方式1  自己写一个新的
        方式2  记住functools 模块的partial()函数
         import functools
         newF = functools.partial(函数, 特定参数=偏爱值)


    使用场景
    int()    一个字符串转换为数值
    numStr = "100010"
    resu = int(numStr, base = 2)
    print(result)


     import functools
    int2 = functools.partial(int, base=2)



"""


def test(a, b, c, d=1):
    print(a + b + c, d)


test(1, 2, 3)


def test2(a, b, c, d=2):
    test(a, b, c, d)

import functools
func = functools.partial(test, a=1, b=3, c=6)
func()

int()