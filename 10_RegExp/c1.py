# 10-1 正则表达式 - 初识findall
'''
正则表达式需要经常拿出来复习！
因为，一旦不经常使用，遗忘超快！
'''
import re

a = "C|C++|PHP|Python|HTML|Javascript"

# 以列表的形式返回结果
r = re.findall('Python',a)
print(type(r))
print(r)