a = []
a.extend([1, 2, 3, 4, 5, 6])
print(a)

del a[3:]
print(a)

# test1
lis = [2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, '1']], 89, 'ab', 'adv']]
print(lis)

# 1)将lis中的tt变成大写(使用两种方式)
lis[3][2][1][0] = 'TT'
# lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)

# 2)将列表中的数字3变成字符串’100’（用两种方式）。
lis[1] = '100'
lis[3][2][1][1] = '100'

# 3)将列表中的字符串’1’变成数字101（用两种方式）



# test2
# 5,查找列表li中的元素，移除每个元素的空格，
# 并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
li = ['taibai ','alexC','AbC ','egon',' Ritian',' Wusir','  aqc']
newList = []
for item in li:
    elem = item.strip()
    if(elem.startswith('A') or elem.startswith('a') or elem.endswith('c')):
        newList.append(elem)
print(newList)



# test3
# 6、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师","东京热",”武藤兰”,”波多野结衣”]
# 则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

li=["苍老师","东京热","武藤兰","波多野结衣"]
new_li= []
while True:
    info = input("评论")  # 苍老师，东京热 法律框架第三
    for i in li:
        if i in info:
            l = len(i)
            info=info.replace(i,'*'*l)
    new_li.append(info)
    print(new_li)
