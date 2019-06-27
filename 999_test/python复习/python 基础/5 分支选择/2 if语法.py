"""
    If语法 & 示例

    单分支判断
            if 条件:
                条件满足时，执行的语句

    双分支判断
            if 条件:
                条件满足时
            else:
                条件不满足时，执行语句

    多分支判断
            if 条件:
                条件满足时，执行语句。。
            elseif 条件：
                条件满足时，执行语句
            （可以重复多次）
            else:
                以上都不满足执行语句

    if嵌套


    注意
        强制缩进  tab缩进
        嵌套   if else 匹配问题
                按照缩进格式进行匹配
        建议  不要写嵌套层级太深的代码
        python中没有类似于其他语言中的switch  case



"""

# age = 10
# if age > 2:
#     print("hello")
# print('赶紧回家吃饭')


#  练习根据分数区间 打印出对应的级别
#  可是有一个小问题    如果分数已经满足了一个条件 是否还有必要判断另外一个那？
#  所以这就是多分支判断


import random

score = random.randint(30, 101)

if 90 <= score <= 100:
    print("优秀")
if 70 <= score < 90:
    print("良好")
if 60 <= score < 70:
    print("及格")
if 0 <= score < 60:
    print("不及格")
print(score)