"""

闭包
    在函数嵌套的前提下
    内层函数引用了外层函数的变量 (包括参数)             这个内层函数+所引用的变量 称为闭包
    外层函数又把内层函数当做返回值进行返回

标准格式
    。。。。。

应用场景
        外层函数 根据不同参数  来生成不同作用功能的函数

案例
        根据配置信息  生成不同的分割线函数


注意事项

        1 闭包内  如果要修改引用的外层变量
                        需要使用   nonlocal  2 变量 声明
                        否则  当做是比包内  新定义的变量


        2 当闭包内  引用了一个  后期会发生变化的变量是  一定要注意




"""


def test():
    a = 4

    def test2():
        print(a)
        b = 666

    return test2


newFunc = test()
newFunc()


def line_config(content, length):
    print("-" * (length // 2) + content + "-" * (length // 2))


line_config("llo", 40)
line_config("llo", 40)
line_config("llo", 40)


def line_config2(content, length):
    def line():
        print("-" * (length // 2) + content + "-" * (length // 2))

    return line


line1 = line_config2("helloworld", 40)
line1()
line1()


# nonloacl  演示

def ltest():
    num = 10

    def ltest2():
        nonlocal num
        num = 666
        print(num)

    print(num)
    ltest2()
    print(num)  # 说明内部的变量是一个新的变量  修改不影响外部变量的值  可以使用nonlocal修改

    return ltest2


ltest()


# 注意2

def test2():
    a = 1

    def test():
        print(a)  # 现在才是一个标识   并没有被执行   不会去找a的值

    a = 2

    return test


newFu = test2()
newFu()


# 一个更复杂的演示
def hello():
    funcs = []
    for i in range(1, 4):
        def test():
            print(i)

        funcs.append(test)
    return funcs


new = hello()
new[0]()
new[1]()
new[2]()

# 上演示  改
def he():
    funcs = []
    for i in range(1, 4):
        def test(num):
            def inner():
                print(num)
            return inner
        funcs.append(test(i))
    return funcs


new = he()
new[0]()
new[1]()
new[2]()





#
# #  演示   。。。。
#
# def hel():
#     print(m)
#
# print("xxxx")
# # 当函数执行时内部的标识符 才回去查找对应的值
# # 函数什么时候才会确定内部  变量标识符    对应的值
# # 当函数调用时 才会真正确定 对应的值   到底是什么  之前 都是以普通标识名称而存在的
#
# hel()
