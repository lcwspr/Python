"""
    以追加的方式(只读)打开文件
    文件的指针将会放在文件的结尾  所以写入内容将会新增到文件的末尾
    注意   文件不存在将会自动创建一个文件


"""


# 1 打开文件

# 相对路径 相对于哪一个目录下面的指定文件
# 以追加的方式写入数据
f = open("src/b.txt", "a")

# 2 读写操作
f.write("\n hello world")

# 3 只能够写  不能够读取
# f.read()


# 关闭文件
f.close()
