# Python 命名空间和作用域窥探

## namespace and Scope

### Namespcae
'''
    从名字到对象的一个映射。大部分namespace都是按Python的字典来实现的

    从某种意义上说，一个对象的全部属性也构成了一个namespace。在程序执行期间，肯定会有多个空间同时存在，不同的namespace的创建/销毁时间也不同
    此外两个不同的namespace中的两个相同名字的变量之间没有任何联系
'''
### scope
'''
    scope是Python中的一块文本区域，在该文本区域内，对于namespace是可以直接访问的，而不需要通过属性来访问
    scope是定义程序该如何搜索确切的  名字-对象  的名空间的层级关系
'''

### Tip
'''
    直接访问： 对于一个变量名的应用会在所有的namespace中查找该变量，而不是通过属性访问。
    属性访问：所有名字后加.都被认为是进行属性访问  如module_name.func_name,需要指定func_name的名空间，属于属性访问
    
    Python中，scope是由namespace按照特定的层级结构组合起来的
    scope一定是namespace，但是namespace不一定是scope
    
    
'''





























