#变量作用域 -- 初识

def demo():
    c = 50  # 局部变量
    for i in range(0,9):
        # 没有块级作用域这个概念
        a = 'a'   
        c += 1
    print('a = ' + a)
    print('c = ' + str(c))

demo()

    