import os
import shutil




# 创建文件
# 直接写入就会自动创建
os.mknod("")

# 创建目录
os.mkdir("")  # 创建单级目录
os.mkdirs("") # 创建多级目录



# 删除目录  文件
os.remove("")   # 删除文件
os.rmdir("")    # 删除文件
os.removedirs("")  # 删除多个文件夹


# 判断
# 判断路径是否存在
os.path.exists("")

# 判断文件是否是目录  文件
os.path.isdir("")    # 目录
os.path.isfile("")   # 文件

os.path.isabs("")   # 是否是绝对路径




# 获取
# 获取python脚本当前的工作空间
pwd = os.getcwd()


# 返回指定目录下的所有文件和目录名
os.listdir("")

# 返回路径的目录名和文件名
os.path.split("路径")
# 结果    ("目录名", "文件名")

# 获取文件属性
os.stat("file")

# 获取文件大小
os.path.getsize("")



# 分离拓展名
os.path.splitext("")

# 获取路径名
os.path.dirname("")

# 获取文件名
os.path.basename("")




# 修改
# 重命名目录
os.rename("old", "new")

# 修改文件权限和时间戳
os.chmod("file")

# 终止当前进程
os.exit()



#  环境相关

# 运行shell命令
os.system("")


# 获取 设置  环境变量
os.getenv("")
os.putenv("", "")

# 给出平台使用的行终止符
os.linesep

# 指出工作平台
os.name




# 目录操作

os.mkdir("")   #  创建目录

# 复制文件
shutil.copyfile("old", "newfile") # oldfile 和 newfile都只能是文件

shutil.copyfile("old", "new")   # old只能是文件夹   newfile可以是文件 可以是目录

# 复制文件夹
shutil.copytree("olddir", "newdir")   # 都只能是目录  新路径必须不存在

# 重命名文件夹
os.rename("src", "old")

# 移动文件
shutil.move("old", "new")


# 删除文件
os.remove("file")

# 删除目录
os.rmdir("")   # 删除空目录
os.removedirs("")   # 同时删除父目录

shutil.rmtree("")  # 删除目录树

# 转换目录
os.chdir()  # 环路径




























