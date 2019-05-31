import  requests
from bs4 import BeautifulSoup
url='http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/qtq/index.html'
req=requests.get(url)
res=req.content
soup=BeautifulSoup(res,'lxml')
node=soup.select(".itemlist")
print(node)
