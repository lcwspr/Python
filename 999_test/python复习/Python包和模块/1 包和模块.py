"""
    python
    包   模块

    概念解释
    包和模块的作用
    包和模块的分类
    包和模块的一般操作
    包和模块的高级操作
    包和模块补充
    虚拟环境



        概念
                模块
            为了使代码更容易维护  提高代码重用价值  可以将一组相关功能的代码写入一个单独的.py文件   供别人导入使用  这个.py文件就被称作是一个模块

                包
            包是一个有层次的文件目录结构 它定义了由n个模块或者n个子包包含_init_.py 文件的目录  这个目录下一定得有这个_init_.py 文件和其他模块或者子包

                库
            参照其他变成语言的一个叫法
            完成一定功能的代码集合
            具体表现可以是一个模块 也可以是包


                框架
            一个架构层面的概念
            从库功能的角度来看  解决一个开放性问题而设计的就具有一定约束性的支撑结构
            通过一个框架，可以快速实现一个问题解决的骨架到时候按照框架的角色去填充 交互就可以完成一个质量好 维护性高的项目

            例如 web框架
                    Flask      (fu la si k)
                    Django      (zhan gou )


"""




"""
为什么要有包和模块  
print(19)
print(12)
print(15)
print(13)


print(12)
print(12)

代码冗余度很高  所以可以封装成函数  
但是可能会有很多相似的函数  文件显得特别散  
所以可以使用类来封装


但是如果有很多类  并且类的功能是有的相似 有的不相干的
例如
class Tool
class Tool1
class Tool3

class Animal
class Dog
class Cat

这样文件比较杂乱  难以 维护代码  想要修改不同的类需要进入相同的文件
但我有时候需要使用一个类    如果你给我这样一个文件 我必须将很多无关类加载进内存

所以  这样 有了模块
.py文件   就是封装了一组相关的类

一个模块为a_module
import a_module

a_module.Tool.t1()


python Package   包
跟普通的文件夹  相似  但是有一个_init_.py

如果有的时候 我需要两个模块a b才能完成相关的功能   a模块需要导入b模块
于是  就有了包   

这个包里面 还能够创建子包





"""








































