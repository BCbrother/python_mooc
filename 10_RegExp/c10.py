# 正则表达式 - re模块下的其他函数（2）
'''
re.sub进阶：函数也可以当做re.sub中的参数进行替换
举例：
    替换字符串s中所有大于等于6的数字，替换为9
    同时，替换s中所有小于6的数字，替换为0
'''
import re

# 函数作为参数，进行灵活的替换
def convert(value):
    # print(value)
    matched = value.group()
    if int(matched) >= 6:
        return '1'
    else:
        return '0'

s = "ABC3721D86"
r = re.sub('\d',convert,s)
print(r)