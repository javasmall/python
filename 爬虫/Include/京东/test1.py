import requests
from  bs4 import BeautifulSoup
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
url='https://search.jd.com/Search?keyword=%E7%A9%BA%E8%B0%83&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=2.def.0.V11&wq=kongtiao&cid2=794&cid3=870&stock=1&page=9&s=222&click=0'
url2='https://so.m.jd.com/ware/search.action?keyword=%E7%A9%BA%E8%B0%83&searchFrom=home&sf=19&as=0&filt_type=ico,L424390M424390;'
url3='http://search.suning.com/%E7%A9%BA%E8%B0%83/'
res=requests.get(url3,headers=header)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'lxml')
link=soup.find(attrs={'class':'general clearfix'})
li=link.select("li")
a=[]
for date in li:
    print(date)
    price=date.find(attrs={'class':'price-box'})
    print(price)
    break