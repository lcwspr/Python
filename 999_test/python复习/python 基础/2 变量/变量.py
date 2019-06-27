"""
    1 什么是变量
        是一个存储数据的容器

    2 变量的特性
        引用着某个具体的数值
        并且可以改变这个引用

    3 变量的定义
        方式1
            变量名 = 值

        方式二
            变量名1， 变量名2 = 值1， 值2

        方式三
            变量名1 = 变量名2 = 值


      4 变量的注意事项

        1 一个变量只能够引用一个数值
        2 变量名使用之前一定要赋值
        3 变量的命名规范


      5 变量的命名规范

        字母数字下划线
        见名知义
        驼峰标识
        非关键字
        区分大小写


      6 查看所有的关键字

        import keyword
        print(keyword.kwlist)



"""
#
# a = 20
# print(a)

#
# a, b = 30, 50
# print(a, b)
# a, b = b, a
# print(a, b)

# a = b = c = d = 30
# print(id(a))
# print(id(b))


"""
    数据类型
        对程序处理的数据进行分类 
        比如说
        1   "abc"
        
    为什么区分类型
        1 区分存储空间
        2 根据不同数据类型的特性  进行不同的数据处理
    
    
    Python 常用数据类型
    
        Numbers(数值类型)    int  long  float  complex
        Bool(布尔类型)    True  False
        String(字符串类型)  ""  ''   ''''''   “”“”“”
        List(列表)
        Set(集合)
        Tuple(元祖)
        Dictory(字典)
        NoneType(空类型)
    
    
    判断数据的类型 type()函数
    
    
    
"""

print(type(3))
print(type("""hello"""))
print(type([]))
print(type({}))

"""
    不同的类型之间不能进行运算
    可以调用类型转换函数 进行不同类型数据间的转换
    
    int(x)  将x转换为整数
    float(x) 将x转换为浮点数
    str(x)  将x转换为一个字符串
    repr(x)  将x转换为一个表达式字符串
    chr(x)   将x转换为一个字符
    unichr(x)  将x转换为一个unicode字符
    ord(x)   将字符x转换为对应的整数值
    hex(x)   将x转换为一个16进制字符串
    oct(x)   将x转换为一个8进制字符串
    eval(str)  计算字符串中的有效表达式 并返回对象
    tuple(s)   将序列S转换为一个元祖
    list(s)    将序列S转换为一个列表
    
    

"""

# print(ord("\n"))


"""
    
    动态类型 或  静态类型
        动态类型   类型是运行的时候判定的 后期可以动态的修改
        静态类型   类型时编译的时候确定的 可以动态的修改
        
        
    弱类型  或 强类型 
        强类型   类型比较强势  不轻易随着环境的改变而改变
        弱类型   类型比较柔软  不同的环境 很容易被改变
        
    
    总结  Python 属于 强类型 动态类型语言
    
"""

#
# print(-10 >> 1)
# m = -10
# for x in range(1, 20):
#     t = m & 1
#     print(t, end='')
#     m = m >> 1
#
# print()
#
# z = -5
# for x in range(1, 20):
#     t = z & 1
#     print(t, end='')
#     z = z >> 1
