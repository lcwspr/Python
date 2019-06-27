"""
匿名函数
        概念 也称为 lambda函数         就是没有名字的函数
        语法
                lambda 参数1, 参数2, :表达式

                限制
                        1 只能写一个表达式  不能直接return
                        2 表达式的结果就是返回值
                        3 所以， 只适用于一些简单的操作处理


        测试



"""

result = (lambda x, y: x+y)(1, 2)

print(result)

newFunction = lambda x, y: x+y

# 还是排序
result = sorted(l, key = lambda x: x["name"])

print((lambda x, y: x * y + 3)(3, 4))















