str='adgddsgsgs'
print(str[0:2])
print(str[1:])#1到最后一个
print(str[0:-2])#0到倒数第二个
print(str[0:5:2])#首尾和 跳的间隔

str="hello zhang sai"
print(str.find('zhang',0,12))#如果为false返回-1
#str.index()用法一样。如果错误会报异常

str='zhang zhang zhang sai sai'
print(str.count('zhang'))
print(str.count('sai',0,12))

name="aa aa aa aa bb"
name=name.replace('aa','cc')#老字符串，新字符串
print(name)
name=name.replace('cc','aa',2)#最多替换两次
print(name)

str='ha hah hhahah hha'
str1=str.split(' ',2)#数组
print(str1[1])

str=str.capitalize()
print(str)#第一个字符大写
str=str.title()
print(str)#每个单词开头都大写

#str.startswith('Ha') bool类型
#str.endswith('Hha')

print(str.lower())
print(str.upper())

#左右对齐，居中
print(str.ljust(40))
print(str.rjust(50))
print(str.center(50))
#mystr.lstrip() mystr.rstrip() 左右字符串去除空格
print('                sg  dg   '.strip())

#rfind rindex
print(str.rfind('ha'))#右侧开始找

#partition rpartition  splitlines(按照行分割) str.isalpha()是否全是字母  是否全是数字
#isalnum 字母或数字  isspace只包含空格

name=['zhang','sao','hfs']
str3='='
str3=str3.join(name)
print(str3)#相当于name后面加str3构成新字符串
