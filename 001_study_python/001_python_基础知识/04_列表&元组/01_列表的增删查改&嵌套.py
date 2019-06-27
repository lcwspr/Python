# 列表
li = ['first',[1,2,3] ,'two', 'three', 'four', 'five']
print(li[0])
print(li[1])
print(li[0:3])

# 增加操作
li = [1, 2, 3, 4]
print(li)
# append    没有返回值None
li.append(5)
li.append([8, 9, 10])
print(li)

# insert
li.insert(2, 'helloworld')    # def insert(self, index, p_object)
print(li)

# extend
li.extend('我叫做lcwspr')
print(li)



'''
while 1:
    username = input('>>>')
    if username.strip().upper() == 'Q':
        break
    else:
        li.append(username)
print(li)
'''


# 删除操作
li = ['first', 'second', 'third', 'four', 'five']
name = li.pop(0)
print(name, li)
name = li.pop() # 默认删除最后一个
print(name, li)

# remove
li.remove('four') # 按照元素删除
print(li)

#clear 清空
li.clear()
print(li)

# 删除整个列表  del语句
# del li
# 删除列表多少以后的(前面的) del li[2:]   del li[0:2]

# 改
li = ['fist', 'second', 'third', 'four', 'fifty']
li[0] = 'hello world'
print(li)

# 切片修改  必须使用可迭代对象
li[0:2] = "hello"
print(li)

# 查
li = ['fist', 'second', 'third', 'four', 'fifty']

for i in li:
    print(i)

print(li[0:2])

# 公共方法
l = len(li)
print(l)

num = li.count('hello')
print(num)


# 排序
li = [1,34,2,38,44,23]
li.sort()
print(li)
# 倒序  li.sort(reverse=True)

# 反转
li.reverse()
