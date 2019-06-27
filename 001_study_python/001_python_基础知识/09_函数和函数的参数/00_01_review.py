# 文件处理


# 打开文件
f = open('file/test.txt',mode='r+',encoding='utf-8')
    # r w a  r+  w+  a+           b
    # 一般情况下都使用单一的方式操作文件

# 操作文件
    # 读
        # read  一次性读取
        # readlines  一次性读

        # readline  一行一行读
            # 不知道在哪结束
            # 视频 图片 rb bytes  按照字节读取
        # 使用for循环  最好
    # 写
        # write

    # 光标    文件指针
        # seek          指定光标移动到某个位置
        # tell          获取光标哦当前的位置
        # truncate      截取文件

f.read()
# 关闭文件
    # close

# 修改文件
    # 注意文件是不能修改的

with open('file/test_modify.txt', mode='r', encoding='utf-8') as f, open('file/modify.bak',mode='w', encoding='utf-8') as f2:
    for line in f:
        if 'lcwspr' in line:
            line = line.replace('lcwspr', 'haijiao')
        # 写文件
        f2.write(line)

# 删除文件和重命名
import os
# os.remove('路径')
# os.rename('a,to', 'b')






























