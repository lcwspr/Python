"""
    python 程序能用很多方式处理日期和时间 转换日期格式是一个常见的功能
    常见操作
        time    模块
            提供了处理时间和表示之间转换的功能

            获取当前时间戳
                概念   从0时区的1970年1月1日0时0分0秒 到所给定日期时间的秒数            浮点数
                获取方式
                        import time
                        time.time()

            获取时间元组
                    概念 很多Python时间函数将时间处理为9个数字的元组
                    图解
                            序号    含义        属性      值
                            0       4位数年     Tm_year   2008
                            1        月         tm_mon    1-12
                            2        日          tm_mday   1-31
                            3         小时        tm_hour   0-23
                            4         分钟        tm_min   0-59
                            5          秒         tm_sec   0-61 (60或61 是闰秒)
                            6          一周第几日   tm_wdat  0-6 0是周日
                            7           一年的第几日 tm_yday  1-366()
                            8            夏令时      tm_isdst  -1,0,1,-1   是决定是否为夏令时的标记
                获取方式
                    import time
                    time.localtime([seconds])   seconds  默认当前的时间戳  可以指定一个时间戳


            获取格式化的时间
                获取格式化的时间
                秒-----可读时间
                    import time
                    time.ctime([seconds])
                    seconds
                            可选的时间戳
                            默认当前时间戳

                    时间元组---可读时间
                    import time
                    time.asctiom([p_tuple])
                    p_tuple
                            可选的时间元组
                            默认当前时间元组



            格式化日期字符串  到  时间戳
                    时间元组 ---- 格式化日期
                        time.strftime(格式化字符串，时间元组)

                        例如
                            time.strftime("%Y--%m--%d  %H:%M:%S", time.localtime())


                    格式化日期 ---时间元组
                    time.strptime(日期字符串，格式化字符串)   将时间字符串 格式化为时间元组

                            例如 time.strptime("2018--09--02  01:38:21","%Y--%m--%d  %H:%M:%S")  必须使用对应的格式字符串


                    time.mktime(时间元组)     将时间元组转换为时间戳


                    常用格式符。。。。


            获取当前cpu时间
                time.clock()       浮点数的秒数
                可用来统计一段代码的程序的执行消耗

                start = time.clock()
                for i in range(0, 10000):
                    print("hello")

                end = time.clock()
                print(end-start)



            休眠n秒
                    推迟程序的执行   可简单理解为  让程序暂停
                    time.sleep(secs)




        calender 模块
            提供了日历相关的功能  比如 为给定的月份呢或年份打印文本日历的功能
            获取某月日历


        datetime 模块
            Python 处理日期和时间标准库
                这个模块有 datetime类    此外常用的还有date类 以及time类
                可以进行一些计算之类的 操作

                获取当天日期
                单独获取当前的年月日时分秒
                计算两个日期的天数差
                获取两个日期时间的时间差
                计算n天之后的日期

"""



import time

print(time.time())
result = time.localtime()
print(result[8])


t = time.time()
result = time.ctime(t)
print(result)


time_tuple = time.localtime()
result = time.asctime(time_tuple)
print(result)

print(time.strftime("%Y--%m--%d  %H:%M:%S", time.localtime()))












