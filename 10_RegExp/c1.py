# 10-1 正则表达式 - 初识
import re

a = "C|C++|PHP|Python|HTML|Javascript"
r = re.findall('Python',a)
print(type(r))
print(r)