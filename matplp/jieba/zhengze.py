import re
pattern=re.compile(r'\d*-\d*-\d*.*')
pattern2=re.compile(r'(\d+):(\d+):\d')
pattern3=re.compile(r'(\S+)(\()(.*?)(\))')#匹配    2班某某(1315426911)相关内容
pattern4=re.compile(r'(\S+)[<].*[>]')
string="2018-05-05 15:55:40 2班某某(1315426911)"
str=pattern3.search(string)
print('威武',str.group(1))
str2=pattern2.search(string)
info={}

# info[str.group(2)]={}#要先声明
# info[str.group(2)]['name']=str.group(1)
# info[str.group(2)]['qq']=str.group(2)
# print(info['1315426911']['name'])
# if('ga' in info.keys()):
#     print(info['ga'])
# print(str2.group(0),str2.group(1),str2.group(2))
#
# string2="2018-05-07 13:48:39 2XXX<xxxx@qq.com>"
# str3=pattern4.search(string2)
# print(str3.group(0),str3.group(1))

