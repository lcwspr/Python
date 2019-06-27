'''
    enumerate() 函数可以将一个可遍历对象(如 列表、元组、字符串)，组合为一个索引序列，同时列出数据和数据的下标，一般用在for循环中
    语法 ：  enumerate(sequence, [start=0])

        sequence   一个序列，迭代器或者其他支持迭代的对象
        start      下标其实位置
'''

l = ['first', 'second', 'third', 'fourth', 'fifth']
pos_l = enumerate(l, 1)
print(pos_l)
print(list(pos_l))

# 普通for循环
i = 0
seq = ['one', 'two', 'three']
for elem in seq:
    print(i, seq[i])
    i += 1

# 使用enumerate()函数
for i, elem in enumerate(seq):
    print(i, elem)