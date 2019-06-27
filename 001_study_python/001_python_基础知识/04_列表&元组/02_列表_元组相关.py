# 列表的嵌套

li = ['first', 'second', 'third', 'four', [1, 2, 3, 4, 5], 'fifty']

print(li[1][1])


# 元组
# 元组被称为只读列表，即数据可以被查询，但不能被修改，所以，字符串的切片操作同样适用于元组，例如(1,2,3),可以循环查询，可以切片。
# 注意儿子不能够修改，但是孙子可能可以改

tu = (1, 2, 3, 'lcwspr', [2, 3, 4, 'good job'], 'good')

print(type(tu))

print(tu[3])

print(tu[0:4])

for i in tu:
    print(i)

tu[4][3] = tu[4][3].upper()
print(tu)

tu[4].append('hello world')
print(tu)

# 元组的两个方法
# index   找到元素的索引
# count    获取某元素列表中出现次数


# 字符串方法join
s = 'lcwspr'
s = '_'.join(s)
print(s)

li = ['first', 'second', 'three', 'four', 'fifty']
s = '_'.join(li)
print(s)

# 字符串转换为列表使用 split
# 列表转换为字符串使用join方法

li = 'hello world'.split()
print(li)


# range  [1, 2, 3, .....end-1]
li = []
for i in range(10):
    li.append(i)
print(li)


li.clear()

for i in range(0, 100):
    li.append(i)
print(li)
li.clear()

for i in range(0, 10, 2):
    li.append(i)
print(li)
li.clear()


li = [1, 2, 3, 4, 5, 'hello', [2, 3, 4, 5, 'tieba'], 'abcd', ('first', 'two', 'three')]
res = []

def showLi(li):
    for i in li:
        if isinstance(i, list) or isinstance(i, tuple):
            showLi(i)
        else:
            res.append(i)
showLi(li)
print(res)
