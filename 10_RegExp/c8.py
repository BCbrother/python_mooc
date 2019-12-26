# 正则表达式 - 匹配模式参数
'''
re.I - 忽略字母大小写，使表达式能够识别小写
re.S - 匹配任何非空白字符
|    - 在findall()中表示和这个概念
'''
import re

language = "PythonC#\nJavaPHP"

# 说明：先加入了.，排除了换行符；
#       但是后面又加入了re.S，又能够识别换行符
r = re.findall('c#.{1}',language,re.I | re.S)
print(r)