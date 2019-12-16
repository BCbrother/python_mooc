# 10-2 正则表达式 - 查找
'''
寻找字符串中的所有数字
\pyhont - 普通字符
\d - 元字符：数字
\D - 元字符：非数字
'''
import re

a = "C0C++6PHP7python#9HTML3Javascript"

r1 = re.findall('python',a)
r2 = re.findall('\d',a)
r3 = re.findall('\D',a)
print(r1)
print(r2)
print(r3)