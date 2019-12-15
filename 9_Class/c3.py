# 类和对象
'''
类是现实世界或思维世界的实体在计算机中的反映
它将数据以及这些数据上的操作封装在一起
数据成员 - 体现了对象的特征
方法 - 体现了对象的行为
self - 可以理解为实例化对象的那个对象，此例中理解为sele -> stu1
'''
class Student():
    # 数据成员
    name = ''
    age = 0

    # 方法 - 行为
    def do_homework(self):
        print(self.name + "is doing homework")

stu1 = Student()
stu1.do_homework()
