import re
pattern=re.compile(r'\d*-\d*-\d*.*')
pattern2=re.compile(r'(\()(.*?)(\))')
pattern3=re.compile(r'[(](.*)[)]')
string="2018-05-05 15:55:40 2班某某(1315426911)"

str1=pattern.search(string)
print(str1.group(0))

str2=pattern2.search(string)
print('group(0):',str2.group(0))
print('group(1):',str2.group(1))
print('group(2):',str2.group(2))
print('group(3):',str2.group(3))

str3=pattern3.search(string)
print('group(0):',str3.group(0))
print('group(1):',str3.group(1))

