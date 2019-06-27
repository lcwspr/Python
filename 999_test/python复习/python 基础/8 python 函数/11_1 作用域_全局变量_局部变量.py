"""
    基于命名空间的常见的变量类型

    局部变量
        在一个函数内部定义得变量
        作用域为函数内部
        查看局部变量   locals()

    全局变量
        在函数外部 文件最外层定义的变量
        作用域为整个文件内部
        查看全局变量  globals()

    注意点
        访问原则
                从内到外

        结果规范
                结构规范
                        全局变量
                        函数定义
                                使用   修改
                        后续代码

        全局变量和局部变量重名
                获取     就近原则
                修改  global 全局变量     声明

        命名

"""
a = 999    #  全局的变量

def test():
    a = 1
    a = 3
    print(a)
    def test2():
        # nonlocal a
        a = 10    # test2内部新定义的a  可以通过nonlocal来修改外部的
        print(a)  # 就近访问原则
    test2()
    print(a)


test()



#  2
b = 999
def glo():
    # 这里如果 直接使用赋值表达式 赋值给一个变量 其实是代表 定义一个新的变量
    # nonlocal 只适用于 在闭包内部修改外部的变脸  如果想要在内部修改全局的变量需要使用global
    global b
    b = 3
    print(b)
    c = 23
    print(locals())   # 查看全部的全局变量
    print(globals())


print(b)
glo()
print(b)





# 当函数调用时 才会确定里面的标识符
# 规范来说  全局变量写在文件的最上面
# 还可以使用g_a    来表名全局变量

m = 28

def hel():
    print(m)
    print(z)

z = 34
hel()






























