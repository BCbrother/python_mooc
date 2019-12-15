#默认参数

def printInfo(name,gender='男',age = 28,college='MIT'):
    print("我的名字是：" + name)
    print("我的年龄是：" + str(age) + "岁")
    print("我是 " + str(gender) + '生')
    print("我在" + college + "上学")
    print("~~~~~~~~~~~~~~~~~~~")

printInfo("Bao")
printInfo("Xue",gender='女',age =29,college='AHFU')