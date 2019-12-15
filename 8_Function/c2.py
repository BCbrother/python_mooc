#c2.py Return的用法

def _addNum(x,y):
    sum = x + y
    return sum

def _printResult(code):
    print(code)

a = _addNum(1,2)
b = _printResult("I'm Python")
# 由于_printResult()函数没有返回值，故默认返回值是None，即b的值
print(a,b)