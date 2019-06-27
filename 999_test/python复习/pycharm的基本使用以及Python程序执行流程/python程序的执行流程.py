"""
    python 程序的执行流程
    严格来说 Python是先编译为字节码文件 然后在解释执行的一门语言
    .pyc 文件的主要作用是持久化编译结果 提升下次的执行效率
    会不会被持久化  主要是根据import机制
    也可以通过命令手动编译&持久化   python -m py_compile practice_file.py
    py  pyc 程序都可以根据直接交给解释器解释执行   不过流程不大一样


    如执行一个 a.py 文件
    会先查看源码内部是否有import b
        有：
            查看是否存在编译好的 b.pyc文件

                有：
                    b.pyc 文件存储的源文件修改时间是否等于源文件 b.pyc 真是修改时间

                        是：
                            根据 b 的PyCodeObject 解释执行

                        否：
                            1 编译源码 b 生成结果PyCodeObject
                            2 存储编译结果到 b.pyc 记录源码的最后修改时间
                            3 根据 b 的PyCodeObject 执行


                没有：
                    编译源码 b 生成结果PyCodeObject


        没有：
            编译源码a生成结果PyCodeObject

        根据 a 大PyCodeObject 解释执行


"""