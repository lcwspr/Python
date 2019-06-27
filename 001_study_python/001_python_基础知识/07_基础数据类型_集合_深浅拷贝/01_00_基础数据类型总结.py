# str
s = ' \t \n '
print(s.isspace())  # 判断是否是空白

'''
    列表和字典在循环的时候不要删除里面的东西
'''

# list
lis = [11, 22, 33, 44, 55]
for i in lis:
    del lis[lis.index(i)]
print(lis)


lis = [11, 22, 33, 44, 55]
for i in range(len(lis)):
    # del lis[i]  # 出现越界异常
    pass
print(lis)


# 需求  删除列表中计数位的数
lis = [11, 22, 33, 44, 55]

# method 1
print(lis[::2])

# method 2
i = 0
res = []
while i < len(lis):
    if not i % 2:
        res.append(lis[i])
    i += 1
print(res)


# 字典
dic = dict.fromkeys([1, 2, 3], 'lcwspr')  # 根据可迭代对象生成字典，值为后面的值
print(dic)
dic = dict.fromkeys([1, 2, 3], [])
print(dic)
dic[1].append('lcwspr')                    # 注意， 如果为可变类型值的话，会指向一个
dic[2].extend('good luck')
print(dic)

l1 = []
l2 = l1
l3 = l1
l3.append('a')
print(l1, l2, l3)


# 小练习
dic = {'k1': 'v1', 'k2': 'v2', 'a3': 'v3'} # 删除键中不含有k的键值对
dic1 = {}

# method1
for i in dic:
    if 'k' not in i:
        # del dic[i]   # 迭代字典时， 不能删除字典的键值对
        # 解决我把这些含有k的键值加入到一个列表，循环这个列表，删除字典中的键值
        dic1.setdefault(i, dic[i])

print(dic1)

# method2
l = []
for i in dic:
    if 'k' in i:
        l.append(i)
for i in l:
    dic.pop(i)
print(dic)


# 什么值转换为bool是False
# 0, '', [], (,), {}, set()


# 元组
tu1 = (1)
tu2 = (1,)
print(type(tu1), type(tu2))
tu1 = ([1])
tu2 = ([1],)
print(type(tu1), type(tu2))
# 只有一个元素的元组必须要加，逗号







