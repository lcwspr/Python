import calendar
import sys

print(calendar.month(2019, 7))

import datetime

print(datetime.datetime.today())

f = open("test.txt", "r")

for x in f:
    print(x)

f.close()

import os

# 打开文件
source_file = open("F:/Android.zip", "rb")
dst_file = open("test.zip", "ab")

# 将读取到的内容写入到另外一个文件
# for content in source_file:
#     print(len(content))
#     dst_file.write(content)

finish = 0
n = 0
while True:
    content = source_file.read(1024)
    if len(content) == 0:
        break
    finish += 1024
    n += 1
    if n == 20000:
        n = 0
        print("\r%f%%" % (finish * 100 / (880053 * 1024)), end="", flush=True)
    dst_file.write(content)
print("\r100%")

# 释放文件资源
source_file.close()
dst_file.close()
