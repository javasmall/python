import requests
from bs4 import BeautifulSoup

url='https://blog.csdn.net/qq_40693171'
req=requests.get(url)
res=req.text#html 源码
soup=BeautifulSoup(res,'lxml')#转为bea--对象
node=soup.find(id='mainBox').find_all(attrs={'class':'article-item-box'})
#print(node[1])
for link in node:
    value=link.h4
    print(value.text)

