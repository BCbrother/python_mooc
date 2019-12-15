#可变参数

def demo(param1,*param2,param3=2):
    print(param1)
    print(param2)
    print(param3)

p1 = 'a'
p2 = (1,2,3)
#p2是一个元组，调用的时候也需要加上一个*，组成可变参数传递！
demo(p1,*p2,param3='bao')