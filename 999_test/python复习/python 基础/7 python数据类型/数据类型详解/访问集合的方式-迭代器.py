"""
    概念

        迭代
            是访问集合元素的一种方式

        可迭代对象
            能够被迭代的对象  称为可迭代对象
            判定依据  能作用于for in
            判定方法  import collections
                    isinstance(obj, collections.Iterable)


        迭代器
            是可以记录遍历位置的对象
            从第一个元素开始，往后通过next() 函数进行遍历
            只能往后   不能往前
            判定依据   能作用于next() 函数       next(list)
            判定方法   import collections
                        isinstance(obj, collections.Iterator)


        注意   迭代器  也是可迭代对象  所以也可以作用于 for in


    为什么会产生迭代器?

        1 仅仅在迭代到某个元素时才处理该元素
                在此之前， 元素可以不存在
                在此之后， 元素可以被销毁
                特别适合用于遍历一些巨大的或是无限的集合  例如斐波那契数列
                [1, 1, 2, ...]  给出的仅仅是一个规则

        2 提供了一个统一的访问集合的接口
                可以把所有的可迭代对象 转换成迭代器进行使用
                iter(Iterable)
                    iter(str)
                    iter(list)
                    iter(tuple)
                    iter(dic)



    迭代器的简单使用
                使用next()函数  从迭代器中取出下一个对象  从第一个元素开始
                因为迭代器比较常用    所以在Python中 可以直接作用于 for  in

    注意  如果取出完毕后继续取   会报错  StopIteration
        迭代器一般不能多次迭代   只能使用一次



        生成 迭代器 iter()函数
        使用for  in 方式迭代


"""


dog = ["小黄", "小王", "小李"]
# 1 创建一个可迭代对象
it = iter(dog)
print(it)
# print(next(it))
# print(next(it))
# print(next(it))

for v in it:
    print(v)
