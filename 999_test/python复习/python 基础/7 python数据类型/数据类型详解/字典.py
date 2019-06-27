# 表述一个人的一些信息    姓名  年龄  身高
str1 = "sz,18,180"
infos = str1.split(",")
print(infos)

# 直接使用一个列表表述   但是直接给你一个l  你根本区分不出各个部分代表的什么
l = ['sz', '18', '180']
print(l[0], l[1], l[2])
for x in l:
    print(x, end=" ")

# 字典类型
# 概念   无序的   可变的   键值对集合
"""
    定义方式
        方式1
            {key:valus, key:value...}
                例如 {"name":"sz","age",18}
                
        
        方式2
            fromkeys(Seq,v = None)
            S 有序的集合   元组 列表 字符串
            
                
                    静态方法
                        类和对象都可以使用(静态方法  很牛掰)
                        
                    类调用
                        dict.fromkeys("abc", 666)    {"a":666,"c":666,"b":666}
                        此处的dict  是指字典类型
                        
                
            对象调用
             {"a":34}   dic.fromkeys("abc",666)     {"a":666,"c":666,"b":666}
                此处的dic   是实例化的字典对象（使用一个真是的对象）

    注意点   1 key不能重复     （如果重复了  后值会覆盖前值）   (相同的运算   会得到相同的存储位置)
            2 key必须是任意不可变类型      （如果key是可变的  会计算出另外一个位置）
            
                原因
                    可变类型   
                        列表   字典   可变集合 ...
                    不可变类型
                        数值  布尔    字符串   元组 ...
                    
                    
                    
                    Python的字典 采用的是哈希(hash)的存储方式实现
                    简单的存储过程
                        1 先初始化一个表格  用来存放所有的数据
                            这个表格称之为“哈希表”
                            暂且可理解为我们所学到的列表
                            
                        2 在存储一个键值对的时候  会做如下操作
                            根据给定的key 通过某些操作， 得到一个在 “哈希表”中的索引位置
                                    把key通过“哈希函数”转换成一个整形数字  称为“哈希值”
                                    将该数字对数组的长度取余  区域结果就当做数组的下标
                                        如果产生了冲突   比如  两个不同的key 计算出的索引是同一个  
                                                        则采用开发地址法   通过探测函数查找下一个位置
                                    
                                    
                            根据索引位置  存储给定的“值”
                            
                    简单的查找过程  
                            再次使用哈希函数 将key转换为对应的列表的索引  并定位到列表的位置获取value
                            
    
    存在的意义：
        可以通过 key, 访问对应的值   使得这种访问更具意义
        person["name"]    表述的是获取一个人的姓名
        
    查询效率 得到很大的提升   可以想象“汉字字典”的使用方式
    
    字典的常用操作（无序可变   可以增删查）
    
            增
                    dic[key] = value
                    当key不存在时 即为新增操作
            
            
            删
                    del  dic[key]
                    
                    dic.pop(key[, default])
                    
            
            
            改
                    只能改键 不能改值
                    修改单个键值对    dic[key] = value
                            直接设置 如果key不存在  则新增 存在则修改
                    
                    
                    批量修改键值对    oldDic.update(newDic)
                    根据新字典  批量更新旧字典中的键值对
                    如果旧自顶字典中没有对应的key 则新增键值对
                    
                    
            查
            
                    获取单个值
                    方式1 
                        dic[key]       如果key不存在会报错
                    
                    方式2 
                        dic.get(key[,defalut])
                        如果不存在对应的key   则取给定的默认值default
                        如没有默认值  则为none    不会报错  
                        原字典不会新增这个键值对
                        
                    方式3 
                        dic.setdefalut(key[,defalut])
                        获取指定key对应的值
                        如果key不存在  则设置给定默认值  并返回该值
                        如果默认值没给定 
                        则使用None代替         如 不存在 则加入 
                        
                        
                    
                    获取所有的值
                        dic.values()
                        
                    获取所有的键
                        dic.keys()
                        
                    获取字典的键值对
                        dic.items()
                        
                在2版本中 获取到键 值 集后  就不会随着原字典的改变而改变  
                3版本中 会随着字典的改变而改变
                                      
                    注意  Python 3.0 版本之间关于获取键 获取值  获取item之间的区别
                    Python2  直接是一个列表  可以通过下标进行获取指定的元素
                    Python3 中 是dictionary view objects
                    意味着  当字典发生改变时   字典视图也会发生改变   不支持索引  
                    可以使用list()  函数  将dictionary view objects 获取列表
                    
                    Python2 中  提供了如下方法  
                    viewkeys()
                    viewvalues()
                    viewitems()  
                    
    
    ？？如何查询所有的键 所有的值  所有的键值对  
    ？？解释 dictionary  view  objects 
    
    
    遍历操作
        先遍历所有的key  然后根据指定的key   获取到指定的值
            d = {"name":"sz"...}
            
            1 先获取所有的key
                keys = d.keys()     为一个可遍历的对象
            
            2 遍历所有的key 
                for key in keys:
                    print(key)             
                    print(d[key])
    
    
        2 直接遍历所有的键值对
        
        1 获取  所有的键值对
        kvs = d.items()
        print(kvs)
        
        2 直接遍历 
        for t in kvs:
            print(t)
        for x,t in kvs:
            print(x,t)
    
        
                                    
        计算
        len(info)       键值对的个数     
            
            
        判定
        x in dic
            判定dic中的key  是否存在x
            
        x not in dic
            判定dic中的key  是否不存在x
            
        dic.has_key(key )    已经过期  建议使用in代替
        
             
                  


"""

person = {"name": "sz", "age": 18}
print(person, type(person))
print(person["name"])
print(person["age"])

# 什么叫做不可变的值

num = 10
print(id(num))

num = 20
print(id(num))

# 说明是块不同的内存

hell = [1, 2, 3, 4]
print(hell, id(hell))
hell.append([4, 3, 5])
print(hell, id(hell))

# s = "nume"
# s[2] = 'e'
# print(s)


d = {"name": "lcwspr", "old": 18}
print(d)
d["name"] = "hello"
print(d)

c = {"name": "wolaile"}
d.update(c)
print(d)