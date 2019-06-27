"""
    打开   open函数

        open("文件"，"模式")
            文件
                指定文件路径
            模式
                控制操作模式


        r
        以只读方式打开文件  这是默认模式
        文件的指针将会放在文件的开头
        注意  文件不存在  将会报错


"""
# 相对路径
f = open("src/a.txt", "r")

# 读写操作
# content = f.read()
# print(content)


f.write("333333")
# r 只能读  不能写


# 3 关闭文件
f.close()




























