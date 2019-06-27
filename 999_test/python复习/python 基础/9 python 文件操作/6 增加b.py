"""
    rb
    wb
    ab

    以二进制文件格式进行操作文件的读写
    如果文件是二进制文件  则选择此项

    例如   图片  视频 音频  程序  。。。

    操作二进制一定要加b

"""

# 1 打开xxx.jpg 文件 取出文件的内容  获取内容的前面半部分

# 1.1 打开文件
fromFile = open("src/1.png", 'rb')

# 1.2 读取文件的内容
fromContent = fromFile.read()
print(fromContent)

# 1.3 关闭文件
fromFile.close()





# 2 打开另外一个文件xxx2.png 然后把取出的半部分内容  写入到xxx2.png中
# 2.1 打开目标文件
toFile = open("src/xx2.png", "wb")

# 2.2 写入操作
content = fromContent[0:len(fromContent) // 2]

# 2.3 关闭文件
toFile.close()
