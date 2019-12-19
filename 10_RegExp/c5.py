# 正则表达式 - 数量词
'''
{数字} - 符合多少数量级
{1,3} - 符合1到3之间的次数
* - *前面的字符可以匹配出现 0次 或 无限次
+ - +前面的字符可以匹配出现 1次 或 无限次
? - ?前面的字符可以匹配 0次 或 1次
'''
import re

# 带有数量词的匹配
a1 = 'python 1111java678php'
r1 = re.findall('[a-z]{3,6}?',a1)
print(r1)

# 匹配0次或无限多次
a2 = 'pytho0python1python2'
r2 = re.findall('python*',a2)
r3 = re.findall('python+',a2)
r4 = re.findall('python?',a2)
r5 = re.findall('python{1,2}?',a2)
print(r2)
print(r3)
print(r4)
print(r5)