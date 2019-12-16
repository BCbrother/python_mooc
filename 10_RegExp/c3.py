# 10-3 正则表达式 - 字符集
import re

s = "abc,acc,adc,aec,afc,ahc"

#查找中间字母是 c或f 的字符 - 使用规则：[xx]
r1 = re.findall('a[cf]c',s)
print(r1)

#查找中间字母 不是c和f 的字符 - 使用规则：[^xx]
r2 = re.findall('a[^cf]c',s)
print(r2)

#查找中间字母 c到f 的字符 - 使用规则：[c-f]
r3 = re.findall('a[c-f]c',s)
print(r3)