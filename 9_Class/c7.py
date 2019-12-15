#成员的可见性
'''
公有 Public
私有 Private
'''
class Student():
    sum = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score = 0    # 私有数据成员
        # print("__init__")
    
    def stu_score(self,score):
        if score < 0:
            print("不能打负分！")
            self.__score = 0
        else:
            self.__score = score
    
    def print_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Score: " + str(self.__score))

student1 = Student('Bao',28)
student1.stu_score(60)
student1.print_info()
print(str(student1._Student__score))
print(Student.__dict__)