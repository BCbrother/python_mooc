# 静态方法 - staticmethod
'''
静态方法
@staticmethod
def function_name():
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
        self.__class__.cnt += 1
        # print("当前班级人数: " + str(self.__class__.cnt))
    
    # 静态方法 须增加装饰器:@staticmethod
    @staticmethod
    def plus_add(x,y):
        # print(Student.cnt)
        print(self.name)
        # print("This is a static method")
        
# 实例化对象
s1 = Student('Bao',28)
s1.plus_sum()
Student.plus_sum()
s1.plus_add(1,2)
Student.plus_add(3,4)