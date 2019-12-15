#关键字和关键参数

def _add(x,y):
    print("x = {},y = {}".format(x,y))
    result = x + y
    return result

#关键参数可以指定参数顺序
sum = _add(y=2,x=1)
print(sum)