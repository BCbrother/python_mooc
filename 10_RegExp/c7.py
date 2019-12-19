#正则表达式 - 字符组合的重复
'''
() - 通过该形式就能完成某一个字符组合的匹配
'''
import re

a = 'PythonPythonPythonPythonPython'

r = re.findall('(Python){2}',a)
# r = re.findall('PythonPython',a)
print(r)