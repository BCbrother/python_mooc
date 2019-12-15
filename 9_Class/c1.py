# 类的定义
'''
有意义的面向对象的代码
面向对象：类、对象
类的实例化
'''

class Student():
    name = 'bao'
    age = 0
    def print_info(self):       #类中定义的函数需要加上self
        print('Name: ' + self.name)       
        print('Age: ' + str(self.age))  

# 类的实例化，已放在c2.py中调用该类，并执行
# student = Student()    
# student.print_info()

