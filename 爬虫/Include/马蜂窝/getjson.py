import requests
from bs4 import BeautifulSoup
url='https://www.mafengwo.cn/mdd/base/list/pagedata_citylist'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
data={
    'mddid':'14387',
    'page': '5'
}
req=requests.post(url=url,data=data,headers=header)
html=req.content
print(html.decode('unicode_escape'))
print(req.json())