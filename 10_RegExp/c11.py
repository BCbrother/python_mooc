# 正则表达式 - re模块下的其他函数（3）
'''
Tips：没有re.findall()函数好用
re.match() - 从字符串首字母开始匹配,找到第一个匹配的结果，以对象形式返回
re.search() - 搜索整个字符串直到找到第一个匹配的结果，以对象形式返回
'''
import re

s = '5269C13D3E19'

r = re.match('\d',s)
print(r)

t = re.search('\d',s)
print(t)