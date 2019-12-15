# 变量的作用域 -- 链式作用域

f = 1   # 优先级：低
def func1():
    f = 2   # 优先级：中
    def func2():
        f = 3   # 优先级：最高
        print(f)
    func2()

func1()
#打印结果是：3