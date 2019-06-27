"""

    除零异常   ZeroDivisionError
        1/0

    名称异常    NameError
            print(name)

    类型异常    TypeError
        "1"+3

    索引异常    indexError
        l = [1, 2]
        l[3]

    键异常     KeyError
        dic = {"name": "sz", "age": 18}
        dic['add']

    值异常     ValueError
        int("abc")


    属性异常        AttributeError
            name = "sz"
            print(name.xx)

    迭代器异常       StopIteration
            it = iter([1, 2])
            print(next(it))
            print(next(it))
            print(next(it))


    系统异常类继承树异常

    BaseException  所有内建的异常的基类
            SystemExit  有sys.exit() 函数引发  当他不处理时  Python解释器退出
            KeyboardInterrupt   当用户点击中断键   时 引发
            GeneratorExit       当调用一种generator 的close() 方法是引发
            Exception          所有的内置的  非系统退出异常 都是从该类派生的
                                应该从该类派生所有用户定义的异常
                子类


    如何解决异常
            系统一开始就已经内置了一些特定的应用场景  当我们写代码的过程中  一点触发了这个场景   系统内部就会自动向外界抛出这个问题  也就是我们所说的异常

            程序被终止执行  软件的崩溃


            预防
                    添加一些容错代码
                    弊端
                    容错代码  不属于我们的主要业务逻辑   如果容错代码过多 会造成代码混乱  主业务逻辑不清晰

            解决

"""


def divide(x, y):
    if y != 0:
        return x / y
    print("除零错误")
    return x / y


try:
    print(name)
except NameError:
    print("名称有问题 请仔细检查")

print(1234)  # 之后的语句 就不会被执行了

"""
    异常的解决  
    捕获处理异常
        
        try
                可能会出现异常的代码  {这里不管以后会抛出到少个异常 只会从上往下检测 检测到一个后  就立即往下去匹配    不会多次检测}

        except 你要捕捉的异常类型  as(python 使用  ,/as  python3 只能使用as)接收异常的形参对于这个异常的处理
        {这一块可以有多个重复 用于捕捉可能的其他异常  如果针对多个不同异常有相同的处理方式 那么可以将多个异常合并}
        
        else:                       这一块必须放在上块except结束后（可以省略）
                没出现异常时做的处理
                
        finally:                    这一块必须放在最后（可以省略）
                不管有没有出现异常  都会执行的代码
                
                
        注意
                try  语句没有捕获到的异常  限制性try 代码段后  在执行else  最后执行finally
                如果try捕获到异常 首先执行except处理错误  然后执行finally
                如果异常名称不确定  而又想要捕捉异常 可以直接写Exception
                
                
        

"""


try:
   # 1 / 0
    print("hello")
except ZeroDivisionError as ze:
    print("xxxx")
except NameError:
    print("名称错误")
else:
    print("123")
finally:
    print("end")



"""
    补充   合并处理
    
"""


try:
    # 1 / 0
    print(name)
except (ZeroDivisionError, NameError) as e:  # 通过一个元祖进行包装  说明匹配的是除零或名称
    print("出现错误", e)
else:
    print("123")
finally:
    print("end")




































