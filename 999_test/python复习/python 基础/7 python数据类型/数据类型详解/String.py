# String

"""
    概念 由单个字符组成的一个集合
    形式  非原始字符串
            1 使用单引号包含的'abc'
            2 使用双引号包含的'abc'
            3 使用三个单引号包含的 ...
            4 使用三个双引号包含的 ...

          元素字符串（就是非原始字符串前加一个r）
            1 使用单引号包含的 r'abc'
            2 使用双引号包含的 r'abc'
            3 使用三个单引号包含的 r...
            4 使用三个双引号包含的 r...

    转义字符     通过转换某个指定的字符    使他具备特殊的含义

    常见的转义符
    在行尾 \        续行符
    \'
    \"
    \t
    \n

    各个形式的特点
    单引号  混合使用可以避免使用引号转义字符
    一般内容需要写成一行 跨行  需要使用连行符  \
    name = "hehhhh"\
    "eeeee"

    可以使用小括号
     (
        name = "hehhhh"\
    "eeeee"
     )

     三引号     1 可以直接跨行书写    2 可用于注释



     字符串的一般操作

     1 字符串的拼接操作
            1 通过加号连接符    str1 + str2
            2 直接把两个加号放在一块   "str1""str2"
            3 字符串模板         "我是%s"%"123"
            4 字符串乘法          "abc"*10



    2 字符串的切片
            1 概念获取一个字符串的某个片段
            2 获取某一个字符
                name[下标]

            下标  注意字符串中每个字符的编号    座位编号
            注意   下标越界
                负数下标   如果有负数 则会从尾部开始 最后一个字符为-1


    len()函数能够获取字符串的长度

    3 获取一个字符串片段
                name[起始索引：结束索引：步长]

                注意：
                    取值范围  [起始,结束)  包含起始 不包含结束

                    默认值
                        起始默认值   0
                        结束默认值  len(name)  整个字符串长度
                        步长默认  1

                    获取顺序
                        步长 > 0  从左到右
                        步长 < 0  从右到左

                注意不能从头部跳到尾部  或者从尾部跳到头部

                特殊案例   翻转字符串 [::-1]


    字符串函数操作
        使用方法 有一部分是内建函数 直接使用 不带小旗子的是属于对象方法
        对象.方法(参数)


            1 查找计算类型的     （内建方法）
                    len()

                        作用
                            计算字符串的字符个数
                        语法
                            len(name)
                        返回值
                            整形
                            字符个数


                    fine()
                        作用
                            查找子串索引的位置
                        语法
                            find(sub, start = 0,end = len(str))
                        参数
                            参数1   sub
                                    需要检索的字符串

                            参数2   start
                                    检索的起始位置
                                    可省略,  默认0

                            参数3   end
                                    检索的结束位置
                                    可省略   默认len(str)

                        返回值
                                找到了
                                    指定索引
                                    整形
                                找不到
                                    -1
                                        注意  从左到右进行查找   找到后立即停止
                                            start end  区间为 半开半闭区间[start, end)
                        相当于是查找


                    rfind()
                    和find() 区别在于从右往左查找


                    index()
                    和find()  一样  区别在于找不到会报出异常
                    相当于是获取

                    rindex()
                    和index()一样    从后往左

                    count()
                        作用
                            计算某个子字符串的出现次数
                        语法
                            count(sub, start = 0, end = len(str))

                        参数
                            参数
                            参数1   sub
                                    需要检索的字符串

                            参数2   start
                                    检索的起始位置
                                    可省略,  默认0

                            参数3   end
                                    检索的结束位置
                                    可省略   默认len(str)

                        返回值
                              子字符串出现的个数
                                            start end  区间为 半开半闭区间[start, end)



            2 转换类方法
                replace()
                    作用
                        使用给定的新字符串 替换元字符串中的旧字符串

                    语法
                        replace(old, new[,count])

                    参数1 需要被替换的字符串
                    参数2 替换后的新字符串
                    参数3 替换的个数    可以省略  默认全部替换

                    返回值  替换后的结果字符串

                    注意  并不会修改源字符串本身

                capitalize()
                    作用 将字符串首字符变成大写
                    语法  capitalize()
                    参数   无
                    返回值  首字母大写后的新字符串
                    注意   并不会修改源字符串

                title()
                    作用 将字符串中每个单次的首字母变成大写
                    语法  title()
                    参数  无
                    返回值  每个单词首字符大写后的新字符串
                    注意  并不会修改源字符串
                        什么是单词    不是字母的符号都视为分割符


                lower()
                    作用 将字符串每个字符都变为小写
                    语法 title()
                    参数 无
                    返回值 全部变为小写后的新字符串
                    注意  并不会修改原字符串

                upper
                    作用 将字符串每个字符都变为大写
                    语法 title()
                    参数 无
                    返回值 全部变为大写后的新字符串
                    注意  并不会修改原字符串



            3 填充压缩操作
                ljust()
                    作用  根据指定字符（1个） 将源字符串填充够指定长度

                    l 原字符串靠左

                    语法  ljust(width,fillchar)

                    参数
                    width:  指定结果字符串的长度     fillchar  如果源字符串长度小于width   填充过去的字符

                    返回值  填充完毕的结果字符串

                    注意  不会修改源字符串
                    填充字符的长度为1
                    只有源len(str)>width  才会填充

                rjust()
                r   表示源字符串靠右
                。。。


                center()
                表示源字符串居中
                不够分的话  就左边少一个  右边多一个



                lstrip()
                    作用  移除所有源字符串指定字符（默认为空白字符）（默认下\n  \t 空白 都为空白）
                        l 表示从左侧开始移除  仅仅只移除左侧的

                    语法 lstrip(chars)
                    参数
                        需要移除的字符集
                        表现形式为字符串
                        "abc"  表示  "a"|"b"|"c"   abc中任何一个都会移除
                    返回值
                        移除完毕的结果字符串
                    注意
                        不会修改原字符串

                rstrip()
                    作用  和lstrip()一样    不过从右边开始检索


            4 分割拼接操作

                split
                 作用   将一个大的字符串分割成一个子字符串

                 语法 split(sep, maxsplit)

                 参数  sep 分隔符
                 maxsplit  最大分割次数    默认为有多少分割多少

                 返回值 分割后的子字符串  组成的列表  list列表类型
                 注意   不会修改原字符串本身

                 info = "sz-18-180"
                 执行分解成四份     分割次数为3     就会分前面的



                 partition
                 作用   根据指定的字符串 返回（分隔符左侧的内容，分隔符，分隔符右侧的内容）元组
                 语法   partition(sep)   从左往右查找
                 返回值
                        如果查找到分隔符
                        分隔符左侧的内容，分隔符，分隔符右侧的内容）
                        tuple  类型

                        如果没有查到分隔符
                        （源字符串，"",""）
                        tuple 类型
                注意  从左侧开始查找分隔符
                        不会修改原字符串


                rpartition

                  作用   根据指定的字符串 返回（分隔符左侧的内容，分隔符，分隔符右侧的内容）元组
                 语法   partition(sep)   从右往左查找
                 返回值
                        如果查找到分隔符
                        分隔符左侧的内容，分隔符，分隔符右侧的内容）
                        tuple  类型

                        如果没有查到分隔符
                        （源字符串，"",""）
                        tuple 类型
                注意  从右侧开始查找分隔符
                        不会修改原字符串



                splitlines
                    作用  按照换行符（\r  \n）  将字符串拆成多个元素   保存到列表
                    语法  splitlines(keepends)
                    参数  keepends    是否保留换行符   bool类型  默认为false
                    返回值 被换行符分割的多个字符串    作为元素组成的列表
                    list  类型
                    注意    不会修改原字符串



                join
                作用 根据指定的字符串  将给定的可迭代对象 进行拼接  得到拼接后的字符串
                语法  join(iterable)
                参数  iterable
                    可迭代的对象   字符串   元祖   列表。。
                 返回值  拼接好的字符串

                可迭代   可以使用for循环遍历的
                items = ["sz", "18","shanghai"]
                result = ",".join(item)

            5 判断操作
            isalpha()
            作用 判断字符串中是否所有的字符都是字母
                不包含数字  特殊符号  标点符号
                至少有一个字符
            语法 isalpha()
            参数 无
            返回值  是否全为字母  bool类型



             isdigit
            作用 字符串中是否所有的字符都是数字
                不包含该字母，特殊符号 标点符号等
                至少有一个字符
            语法 isdigit()
            参数 无
            返回值   是否全为数字  bool类型


            isalnum
            作用 判断字符串中是否所有的字符都是数字或者字母
                不包含  特殊符号  标点符号
                至少有一个字符
            语法 isalnum()
            参数 无
            返回值  是否全为字母或数字  bool类型



            isspace()
            作用 判断字符串中是否所有的字符都是空白符
                包括 空格 缩进     换行  等不可见转义符
                至少有一个字符
            语法 isalnum()
            参数 无
            返回值  是否全为空白符  bool类型



            startswith
            作用  判定一个字符串是否以某个前缀开头
            语法 startswith(prefix, start = 0, end= len(str))
            参数
                prefix   需要判定的前缀字符串
                start    判定的起始位置
                end      判定的结束位置

            返回值   是否以指定的前缀开头    bool类型


            name = "2018-09-02:jjjj.xls"
            name.startswith("2018-09-02")

            start  从第几个元素开始判断



            endswith

            作用  判定一个字符串是否以某个后缀结尾
            语法 startswith(prefix, start = 0, end= len(str))
            参数
                prefix   需要判定的前缀字符串
                start    判定的起始位置
                end      判定的结束位置

            返回值   是否以指定的后缀结尾    bool类型


            name = "2018-09-02:jjjj.xls"
            name.startswith("2018-09-02")

            start  从第几个元素开始判断



            补充：
                in  判定一个字符串，是否被另一个字符串包含
                not in  判定一个字符串是否不被另外一个字符串包含


            总结   字符串操作  很重要  很重要 很重要
            知道一个大概  就可以




"""

name = "lcwspr"
print(name[::2])
print(name)


print(len(name))


name1 = "wo shi sz"
num = name1.find("sz")
print(num)


name1.count("w")





