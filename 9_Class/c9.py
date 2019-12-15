# 类的继承性-2 子类
'''
'''
from c8 import Human

class Student(Human):

    def __init__(self,school,name,age):
        self.school = school
        # 调用父类中的构造函数
        # Human.__init__(self,name,age)   # X 不推荐这种方式
        super(Student,self).__init__(name,age)  # √ 推荐这种方式

    def print_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Score: " + str(self.__score))

    def do_homework(self):
        super(Student,self).do_homework()
        print(self.name + " is doing homework.")
        
# print(Student.sum)
stu1 = Student('NFU','Bao',28)
stu1.get_info()
# print(stu1.name)
# print(stu1.age)
# stu1.do_homework()
stu1.do_homework()
