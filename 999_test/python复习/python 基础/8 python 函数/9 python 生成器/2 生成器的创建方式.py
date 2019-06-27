"""
生成器的创建方式

但是生成的这个列表有可能会被浪费   一下全部加载到内存
如果用到那个数据  就拎出那个数据  这样是不是比较好



"""

# 列表的推导式
l = [i*2 for i in range(1, 10000000) if i % 2 == 0 ]
# 于是 我想要生成一个迭代器
# iter(l) # 但是  这个列表已经存在了  不符合要求
# print(l)

# 于是   借助于迭代器 生成器
t = (i for i in range(1, 10000000) if i % 3 == 0)
print(t)

print(next(t))   # 第一种访问方式
print(next(t))
print(next(t))
print(t.__next__())  # 第二种相似方式

# for x in t:        第三种方式
#     print(x)























