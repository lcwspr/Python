# dict
# 数据类型划分，    可变数据类型，不可变数据类型
# 不可变数据类型    tuple bool int str  不可以更改的就是可哈希的
# 可变数据类型      list dict set       不可哈希的

# dict 的键必须是不可变数据类型，就是必须是可哈希的数据类型(bool,int,tuple,str)
# 值value 可以是任意数据类型

'''
    dict
    优点：
        查询数据快
        存储大量的关系型数据
    特点： 无序的，通过键值对去查找
'''

dic = {
    'name': ['lcwspr', 'top'],
    'py8': [{'num': 71, 'avg_age': 18},
            {'num': 64, 'avg_age': 19},
            {'num': 87, 'avg_age': 16}],
    True: 1,
    (1, 2, 3): 'hello world',
    3: '三哥'
}

print(dic)

dict1 = {'age': 18, 'name': 'hello', 'sex': 'male'}

# 增加
dict1['high'] = 185  # 没有这个键值对，添加
dict1['age'] = 16  # 如果有键则值覆盖

dict1.setdefault('weight')  # 默认添加None
dict1.setdefault('hello', 'I want you good！')  # 有键值对，不做任何改变，没有则添加

print(dict1)

# 删除

# 按照键去删除，返回删除的值
print(dict1.pop('age'))  # 有返回值，按照键去删除
print(dict1)

print(dict1.pop('lcwspr', None))  # 可设置一个没有此键的返回值，这样删除情况下没有这个键不会报错

# 随机删除一个键值对   返回键值元组
print(dict1.popitem())
print(dict1)

# del删除
del dict1['name']
print(dict1)

# 删除整个字典
# del dict1

# 清空键值对
dict1.clear()
print(dict1)

# 修改
dict1 = {'one': 20, 'first': 50, 'three': 89}
print(dict1)

dict1['one'] = 'hello world'  # 如果键相同，值不同则为修改
print(dict1)

# update
# 将dic的内容更新到dict1中，如果有就会修改，如果没有就会增加
dic = {"one": "good", "age": 19, "sex": "male"}
dict1.update(dic)
print(dict1)

# 查询
t = 'sex'
dic2 = {'age': 19, 'name': 'jin', t: 'male'}

print(dic2.keys(), type(dic2.keys()))
print(dic2.values(), type(dic2.values()))
print(dic2.items(), type(dic2.items()))

# 拿到所有的键
lis = []
for i in dic2:  # 相当于dic.keys()
    lis.append(i)
print(lis)
lis.clear()

# 拿到所有的值
for i in dic2.values():
    lis.append(i)
print(lis)
lis.clear()

# 额外知识点
a = 1
b = 2
a, b = b, a
print(a, b)

a, b = [3, 4]
print(a, b)

a, b = {"first": 34, "second": 45}
print(a, b)

# 打印键值对
lis.clear()
for i in dic2.items():
    lis.append(i)
print(lis)
lis.clear()

for k, v in dic2.items():
    lis.append('k = %s, v = %s' % (k, v))
print(lis)
lis.clear()

# 还有一个查的方法  没有这个值会报错
print(dic2['age'])

# get方法   可以设置默认值，不会报错
print(dict1.get('ages', 'no key'))
