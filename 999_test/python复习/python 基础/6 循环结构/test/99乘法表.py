# -*- coding:utf-8 -*-
# 打印一张 9 9 乘法表


for i in range(1, 10):
    for j in range(1, 10):
        if j > i:
            break
        print("%d*%d=%d" % (j, i, i*j), end="\t")
    print(end="\n")



#
# # 1  给定一个数值  打印出 从1 到这个数值间 的所有数字
#
# for num in range(1, 10):
#     # 1 选择一个集合
#     nums = range(1, num + 1)
#
#     # 2 遍历这个集合
#     for n in nums:
#         # 3 在遍历的过程中打印每一个元素
#         print("%d*%d=%d" % (n, num, num * n), end='\t')
#     print()
