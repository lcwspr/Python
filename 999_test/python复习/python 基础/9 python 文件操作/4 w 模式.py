"""
    w 模式
         以只读方式打开文件
         文件的指针会放在文件的开头  所以写入新内容会覆盖
         注意  文件如果不存在 会自动创建一个新的文件


"""

# 1 打开文件

# 相对路径 相对于哪一个目录下面的指定文件
f = open("src/b.txt", "w")

# 2 读写操作
f.write("i lo")

# 3 只能够写  不能够读取
# f.read()


# 关闭文件
f.close()

























































