# 正则表达式 - re模块下的其他函数（1）
'''
re.sub(str,str_sub,str,count=0) - 替换
'''
import re

language = "PythonC#JavaPHPC#"
#将C#换成Swift，最后一个参数表示最多替换的次数
r = re.sub('C#','Swift',language,1)
print(r)