#类方法 - classmethod
'''
类方法
@classmethod
def function_name(cls):
    pass
'''
class Student():
    # 类变量 - 数据成员
    cnt = 0

    # 构造函数 Constructor
    def __init__(self,name,age):
        # 初始化对象的属性
        self.name = name
        self.age = age
    
    # 类方法 增加装饰器
    @classmethod
    def plus_sum(cls):
        cls.cnt += 1
        print(cls.cnt)
        
# 实例化对象
s1 = Student('Bao',28)
Student.plus_sum()
s2 = Student('Xue',29)
Student.plus_sum()
s3 = Student('Youran',1)
Student.plus_sum()