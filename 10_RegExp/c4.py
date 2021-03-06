# 10-4 正则表达式 - 概括字符集
'''
概括性的表示某一组数字、字符等
    \d 或 [0-9] - 匹配数字
    \D 或 [^0-9] - 匹配非数字
    \w - 匹配单词字符、数字字符、下划线，相当于[A-Za-z0-9]
    \W - 匹配非单词字符
        包括：特殊符号 &*# 等
        也包括：回车符/空格符/制表符 等空白字符
    \s - 匹配任何空白字符：回车符/空格符/换行符/制表符等
    \S - 匹配任何非空白字符
    .  - 匹配除换行符\n之外其他所有字符
'''
import re

a = 'pyt hon\t1111&java\r678\nphp'
b = "鲍勃在家666"

r1 = re.findall('\w',a)
print(r1)
r2 = re.findall('\W',a)
print(r2)
r3 = re.findall('\s',a)
print(r3)
# 中文也能匹配
r4 = re.findall('\D',b)
print(r4)