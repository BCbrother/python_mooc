# 类的继承性-1 父类
'''
'''
class Human():
    sum = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_info(self):
        print(self.name)
        print(self.age)

    def do_homework(self):
        print("I'm Father Class")
