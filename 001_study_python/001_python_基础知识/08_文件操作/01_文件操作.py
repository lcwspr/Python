'''
    文件操作
    1. 文件路径  D：\模特.txt
    2. 编码方式  utf-8  gbk
    3. 操作方式： 只读，只写，追加，读写，写读。。。
'''
# 以什么编码方式存储的文件，就以什么编码打开进行操作

# 只读 文本模式      bytes ----> 转化为  str
f = open('test_file/葫芦娃.txt',mode='r', encoding='utf-8')
content = f.read()  # 一下全读出来
print(content)
f.close()

# 只读 二进制模式   用于非文字类的文件的打开操作
f = open('test_file/test.txt',mode='rb')
content = f.read()
print(content.decode('utf-8'))
f.close()


# 只写
f = open('test_file/log.txt', mode='w', encoding='utf-8')
f.write('呵呵呵')
f.close()
# 没有此文件就会创建该文件
# 先将源文件的内容全部清除，再写

# 只写  二进制模式
f = open('test_file/binary_write.txt', mode='wb')
f.write('我真的感觉很好呀'.encode('gbk'))
f.close()


# 追加
f = open('test_file/add_write.txt', mode='a',encoding='utf-8')
f.write('我真的感觉很好呀')
f.close()


# 追加   二进制模式
f = open('test_file/add_binary_write.txt', mode='ab')
f.write('其实真的挺不错的，我感觉很好'.encode('utf-8'))
f.close()

