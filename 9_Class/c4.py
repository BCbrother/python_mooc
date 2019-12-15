# 实例化及其意义 - 构造函数
'''
1.当调用类时，构造函数会被默认执行1次
2.构造函数返回的是None，而不能返回其他值
3.构造函数作用就是让模板生成不同的对象
4.类变量 & 实例变量
'''

class Student():
    # 类变量 - 数据成员
    cnt = 0

    # 构造函数 Constructor
    def __init__(self,name,age):
        # 初始化对象的属性
        self.name = name
        self.age = age
        print("__init__")
        print(self.__class__.cnt)

    # 方法 - 行为
    # 实例方法
    def do_homework(self):
        print(self.name + " is doing homework")

#实例化对象
s1 = Student('bao',28)
print(Student.cnt)      # 类外调用类变量