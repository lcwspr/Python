f = open('showFunc/haha.txt',mode='r+',encoding='utf-8')
f.seek(3)  # 按照字节定光标的位置
print(f.tell()) # 光标的位置在哪
content = f.read(3)     # 读出来的都是字符
print(content)
f.close()

# 读取后三个    count = f.tell(); f.seek(count-3)


# readline()
# truncate()          # 对原文件进行截取    这个东西还是挺有用的
f = open('showFunc/haha2.txt',mode='r+',encoding='utf-8')
print('k')
line = f.readline()  # 一行一行的读取
while line:
    print(line,end='')
    line = f.readline()
print('k')

line = f.readlines()  # 每一行作为列表的一个元素
f.close()



# 可以使用for循环打印file对象
f = open('showFunc/haha2.txt',mode='r+',encoding='utf-8')
for i in f:
    print(i, end='')


# 另外一种文件的打开方式
with open('showFunc/otherway.txt',mode='r+',encoding='utf-8') as f:
    print(f.read())