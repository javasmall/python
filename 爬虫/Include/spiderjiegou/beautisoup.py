html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')


#意思是子节点的所有    enumerate格式化输出（index,str)   list是数组[]形式
for str2 in enumerate(soup.p.descendants):
   print(list(str2))

for str3 in enumerate(soup.p.next_siblings):
    print(list(str3))
#find_all(name, attrs, recursive, text, **kwargs)



