# 集合，可变数据类型，但是它里面的元素必须是不可变数据类型，无序的，不重复的  {}
set1 = set({1, 2, 3})
set2 = {1, 2, 3}
print(set1)
print(set2)

# 增
# add
set1 = {'first', 'second', 'three', 'four'}
set1.add('lcwspr')
print(set1)

# update
set1.update('abc')  # 相当于extend
print(set1)

# 删除
set1.pop()  # 随机删除，有返回值
set1.remove('lcwspr')  # 指定删除
print(set1)
set1.clear() # 清空
del set1

for i in set2:
    print(i)

# 集合操作

# 交集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)
print(set1.intersection(set2))

# 并集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 | set2)
print(set1.union(set2))

# 差集   # set1独有的
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 - set2)
print(set1.difference(set2))


# 反交集，
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 子集 与 超集
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1 < set2)
print(set1.issubset(set2))

print(set2 > set1)
print(set2.issuperset(set1))


# 去重
li = [1, 2, 4, 5, 3, 2, 4, 5, 3, 5, 53, 2]
print(list(set(li)))



# 不可变集合
s = frozenset(set(li))
print(s)