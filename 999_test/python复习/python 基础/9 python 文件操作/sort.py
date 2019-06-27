import os
import shutil
path = "les"

if not os.path.exists(path):
    print("路径不存在")
    exit()

os.chdir(path)
# 0 获取所有的文件名称列表
file_list = os.listdir("./")
print(file_list)

# 1 遍历所有的文件名称
for file in file_list:

    # 2 分解所有的后缀名
    # 2.1 获取最后一个.的索引位置
    index = file.rfind(".")
    if index == -1:
        continue
    # 2.2 以该索引位置切片
    file_type = file[index+1:]



    # 3 查看一下是否存在同名的目录  有跳过  没有就创建
    #     3.1 切换当前目录

    if not os.path.exists(file_type):
        os.mkdir(file_type)

    # 4 移动文件
    shutil.move(file, file_type)

