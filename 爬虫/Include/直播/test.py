import  requests
from bs4 import BeautifulSoup
url='http://m.toubang.tv/'

req=requests.get(url)
soup=BeautifulSoup(req.text,'lxml')


node=soup.select(".item-list")
for li in node:
    print(li.text)