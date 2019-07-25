import requests
from bs4 import  BeautifulSoup
import json
import urllib.parse


url="https://sourceforge.net/u/yuosef1/profile/"
req=requests.get(url)
res=req.text
soup=BeautifulSoup(res,'lxml')


name=soup.find(attrs={'itemprop':'name'}).text


print(name)