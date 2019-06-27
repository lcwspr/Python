"""
    概念 有序的可变的元素集合
    定义
    常用操作
    #
    # 字符串更倾向于将数据当为一个整体  字符串的可以获取  但是不能更改
    # 字符串是一个不可变类型
    #
    # 列表 倾向于 里面的元素本身就是一个一个的个体
    里面的元素是有顺序的  可变是指 这个队伍可以增删查改


    列表的定义：     可以存放任何类型

        方式1
            [元素1， 元素2]    例如 nums = [1, 2, 3, 4, 5]

        方式2
            列表生成式
                语法 1 range(stop) [0, 1, 2,   stop-1]


                    2 range(start, stop, step)
                      生成的列表[start, start+step, start+2*step,    <stop]

                    注意  为了防止生成的列表没有被使用  Python3 中不会立即生成列表


            列表推导式
            从一个list 推导出另外一个list
            概念
                映射解析  一对一变更
                过滤  从多到少
            语法
                [表达式 for 2 变量 in 列表]
                [表达式 for 2 变量 in 列表 if 条件]  条件中还能够嵌套for遍历  能够使元素变多


            案例
                [num ** 2 for num in nums if num % 2 == 0]
        也能够变多[num ** 2 for num in nums for num2 in nums]

        列表的嵌套   列表中的元素   还可以是列表
        注意和c语言数组的区别



        常用操作
            增
                append
                    作用  往列表的最后追加一个新的元素 在列表的最后
                    语法  l.append(object)
                    参数  object 想要添加的元素
                    返回值 None
                    注意  会直接修改原列表


                insert
                    作用  往列表中追加一个新的元素   在指定的索引前面
                    语法  l.insert(index, object)
                    参数
                        index  索引  到时会插入到这个索引前面
                        object 想要添加的元素
                    返回值 None
                    注意  会直接修改原数组


                entend    同类型会合并
                    作用  往列表中 拓展另外一个可迭代序列
                    语法  l.extend(iterable)
                    参数  iterable
                            可迭代的序列
                                字符串
                                列表
                                元组
                                。。。
                    返回值  None
                    注意  会直接修改原数组

                在元列表之后追加




                乘法操作     乘以一个整数  来让列表重复多少次
                    [1, 2] * 3
            #                   [1, 2, 1, 2, 1, 2]



                加法操作
                [1, 2] + [3, 4, 5, 6]
                            [1, 2, 3, 4, 5, 6]
                和extend基本一样    加法运算只能列表类型和列表类型




            删

                del 语句
                    作用  可以删除一个指定元素（对象）
                    语法  del指定元素
                    注意      可以删除整个列表
                            删除一个变量
                            也可以删除某个元素

                    删除一个元素
                    nums = [1, 2, 3, 4, 5]
                    del  nums nums[1]

                    del 变量名  相当于回收内存




                   pop()
                   作用  移除并返回列表中指定索引对应的元素
                   语法  l.pop(index = -1)
                   参数  index 需要被删除返回的元素序列
                            默认是-1   也就对应着列表的最后一个元素
                    返回值   被删除的元素
                    注意   会直接修改原数组     注意索引越界



                    remove()
                    作用  删除列表中的指定元素
                    语法  l.remove(object)
                    参数 object  需要被删除的元素
                    返回值 none
                    注意  会直接修改原数组
                        如果元素不存在会报错
                        如果存在多个元素 那么只会删除最左边的一个

                    注意循环内删除列表元素带来的坑



                    nums = [1, 2, 2, 2, 3, 4, 2]
                    for nums in nums:
                        if num == 2:
                            nums.remove(2)   删除全部的元素  为什么不行那？

                    不要在遍历中  移除所有的相同元素


            改
                name[index] = 666
                当我们以后想要操作一个列表当中的某个元素时， 一定是通过这个索引（下标）,来操作指定元素的
                nums = [1, 2, 3, 4, 5 ]
                nums[2] = 6;


            查
                获取单个元素
                    items[index]   注意负数索引(跟字符串一样)

                获取元素索引   从左到右查找
                    index(value, start=null,end = null)


                获取指定元素个数
                    count()

                获取多个元素
                        切片
                            item[start:end:step]

                遍历元素
                        方式1
                                根据元素进行遍历
                                value = ['a', 'b', 'c', 'd']
                                for item in list:
                                    print(item)

                                如何拿到索引
                                currentIndex = 0
                                for item in list:
                                    print(value.index(item, currentIndex))
                                    currentIndex += 1

                        方式2
                                根据索引进行遍历
                                for index in range(len(list)):
                                    print(index, list[index])

                                1 构造一个索引列表 （我们要查询的 要遍历的索引列表）
                                2 遍历整个索引列表  每一个索引   索引  获取指定的元素




                        方式3
                                创建对应的枚举对象
                                    概念  通过枚举函数 生成一个新的对象
                                    作用  函数用于将一个可遍历的数据对象（如列表  元祖  或字符串）组合为一个索引序列  同时列出数据下标和数据
                                    语法 enumerate(sequence,[start = 0]) sequence  一个序列  迭代器 或其他支持迭代的对象      start  下标起始位置

                                    举例
                                        1 先根据列表  创建一个枚举对象
                                        print(enumerate(list, start, end))
                                        print(list(enumerate(list)))   里面是一个一个的元组

                                        2 遍历整个枚举
                                    for idx,val in enumerate(list):

                                    for tupleValue in enumerate(list):
                                        print(tupleValue[0],tupleValue[1])

                                    可以通过元组的解包
                                    idx, val = tupleValue
                                    idx  val  就是值





                        方式4
                                使用迭代器进行遍历

                        访问集合的方式迭代器
                        import 迭代器.py



            额外操作    (in   not in  针对的是所有的集合)
                    判定
                        元素 in 列表
                        元素 Not in 列表



                    排序
                        内建函数  可以对所有的可迭代对象进行排序
                        语法    sorted(iterable, key = None ,reverse = False)
                        参数    iterable   可迭代对象
                                key 排序关键字    值为一个函数  此函数只有一个参数 且返回一个值用来进行比较
                                reverse    升序
                                false  升序   true降序
                        返回值   一个排好序的列表    列表类型  不管是什么类型 都会是列表

                        s =[("sz", 14),("s", 14),("sz4", 14),("z", 14),("rz", 14)]

                         如果排序的话 会按照元祖的首个元素排序
                         如果想要按照元组第二个值排序  怎么搞

                        使用一个函数
                        def getKey(x):
                            return x[1]

                        result = sort(s, key=getKey)
                        注意   会返回排序好的list集合  但是不会修改原集合
                                可以针对所有的可迭代对象对象




                        排序方式 2
                            列表对象方法
                            语法 list.sort(key = None, reverse = False)
                            参数    iterable   可迭代对象
                                    key 排序关键字    值为一个函数  此函数只有一个参数 且返回一个值用来进行比较
                                    reverse    升序
                                    false  升序   true降序

                            注意  没有返回值 会改变集合本身
                            list 集合方法



                    比较
                            cmp()  内建函数     python2 支持
                            比较字符串  按个比较ascii码
                            如果比较的是列表 则针对每个元素  从左到右逐一比较
                            左   >    右    1
                            左   =    右    0
                            左   <    右    -1
                            python3 不支持



                            Python3 使用比较运算符
                            ==  <  ...


                    乱序
                        可以随机打乱一个列表
                        导入random模块
                            import random
                        random.shuffle(list)
                        直接改变list本身



                    反转
                    list.reverse()
                    改变列表本身


                    切片翻转
                    l[::-1]

                    返回结果


"""
import random


name2 = ["hello", "say you"]
name = ["xiaohoang", "xiaoming", "xiaowang", "xiaoli"]
name.extend(name2)

# random.shuffle(name)
print(name)
print(name.reverse())
print(name)
