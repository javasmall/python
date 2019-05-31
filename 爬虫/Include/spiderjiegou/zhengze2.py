import re
#mathch头部或者指定位置
patten=re.compile(r' ([a-z]+) ([a-z]+)')#中间的空格很重要
m=patten.match(' hello world wofda math')
print(m.group(0))
print(m.span())#整个句子的索引

#search方法
n=patten.search("fmadk25fd262 62fd6s makdgfa hello worlfdfa")
print(n.group())
print('hello',n.span())
print('jlef','efkgeg')

#findall方法
j=patten.findall('heki anjdnf naf k fkjfa')
print(j)#数组
for exam in j:
    print(exam)
