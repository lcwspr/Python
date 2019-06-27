class Person:

    def __init__(self, old=20):
        self.__old = old

    def eat(self):
        print("hello wrold" + str(self.__dict__))

    def setold(self, old):
        if not isinstance(old, int) or old < 0 or old > 150:
            print("数据不合理")
            return
        self.__old = old


class Student:

    def __init__(self, old):
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        if old > 0:
            self.__old = old
        else:
            self.__old = 0

    @old.deleter
    def del_old(self):
        del self.__old

    def __str__(self):
        print(self.__old, end="\n")

    # old = property(get_old, set_old, del_old)


stu = Student(20)
stu.old = 100
print(stu.old)
del stu.old
