import requests
from bs4 import  BeautifulSoup
import json
import urllib.parse


url="https://sourceforge.net/p/corefonts/feature-requests/search/?q=%21status%3Awont-fix+%26%26+%21status%3Aclosed"
req=requests.get(url)
res=req.text
soup=BeautifulSoup(res,'lxml')

title=soup.find(attrs={'class':'long-title','itemprop':'name'}).text
description=soup.find(attrs={'class':'summary'}).text
status=soup.find(attrs={'class':'status-value'}).text
table=soup.find(attrs={"class":"ticket-list"}).tbody

print(title)
print(description)
print(status)
print(table)