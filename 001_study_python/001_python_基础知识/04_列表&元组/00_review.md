## 编码
* ascii：字母，数字，特殊字符，1个字节，8位
* unicode: 16位，两个字节，升级32位，四个字节
    * utf-8: 最少一个字节8位表示，欧洲文字是由16位，两个字节表示，中国文字使用三个字节表示
* gbk：中文2个字节表示，英文一个字节

## int 
bit_length()

## bool
True 
False

## str 
* str ----> bool 非空就是True

* 常用方法
    > capitalize()
    
    > upper()
    
    > lower()
    
    > title()
    
    > find()
    
    > index()
    
    > swapcase()
    
    > replace(old, new ,count)
    
    > isdigit() 
    
    > isapha()
    
    > isnumpha()
    
    > startswith()
    
    > endswith()
    
   
    > center() 
    
    > strip()  lstrip()  rstrip()
    
    > split()
    
    > count()
    
    > len()

## 格式化输入
1. 'hello{}'.format('first')
2. 'he{0}llo{1}'.format(12,'hello')
3. 'hello{first} world{world}'.format(first=34, world='hhh')


## 判断是否在其中
for i in 可迭代对象:
    pass
    
    
## python 字符串标准
* python2 在编译安装的时候，可以通过参数 --enable-unicode=ucs2 或者 --enable-unicode=ucs4 分别用于指定使用2个字节、4个字节表示一个unicode字符
* python3中无法进行选择，默认使用ucs4
* 查看当前python中表示unicode字符串时占用的空间
```
    import sys
    print(sys.maxunicode)
    # 如果值为65535,则表示使用ucs2标准，即两个字节表示
    # 如果值为1114111，则表示使用ucs4标准，即，4个字节表示
```

















