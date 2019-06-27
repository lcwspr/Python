# 1、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
lis = [1, 2, 3, 4, 5, 6, 7, 8]
def getLis(lis):
    return lis[::2]

print(getLis(lis))

# 2、写函数，判断用户传入的值（字符串、列表、元组）长度是否大于5。
def isLong5(ele):
    try:
        if len(ele) > 5:
            return True
    except Exception as e:
        print('请输入正确的数据类型')
        raise Exception('类型错误')
    return False


print(isLong5('fjee'))

# 3、写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果。
def func(s):
    dic = {'num': 0, 'alpha': 0, 'space': 0, 'other': 0}
    for i in s:
        if i.isdigit():
            dic['num']+=1
        elif i.isalpha():
            dic['alpha'] += 1
        elif i.isspace():
            dic['space'] += 1
        else:
            dic['other'] += 1
    return dic

# 4 写一个函数，接收两个数字参数，返回比较大的那个数字
def getMax(a, b):
    if a > b:
        return a
    else:
        return b

# 三元运算符
def getMax2(a, b):
    return a if a > b else b

print(getMax2(3, 25))

# 格式
# 变量 = 条件返回True的结果 if 条件 else 条件为False返回的结果
# 必须要有返回的结果
# 必须要有if else
# 只能是简单的情况


# 5、写函数，用户传入修改的文件名，与要修改的内容，
# 执行函数，完成整个文件的批量修改操作（进阶）。
# def func(filename,old,new):
#     with open(filename, encoding='utf-8') as f, open('%s.bak'%filename, 'w', encoding='utf-8') as f2:
#         for line in f:
#             if old in line:  # 班主任:星儿
#                 line = line.replace(old,new)
#             # 写文件
#             f2.write(line)  # 小护士:金老板
#
#     import os
#     os.remove(filename)  # 删除文件
#     os.rename('%s.bak'%filename, filename)  # 重命名文件
