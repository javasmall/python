import requests
import time
from bs4 import BeautifulSoup 

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
###
def getpage(url):
    pass
    

#获取访客，粉丝等基础信息
def getbaseinfor(url):
    req=requests.get(url,headers=header)
    res=req.text
    soup=BeautifulSoup(res,'lxml')
    node=soup.find(id="asideProfile")
    count=node.dd.span.text#总文章数
    fan=node.select("#fanBox")[0].get('title') #粉丝数
    love=soup.find(attrs={'class':'data-info d-flex item-tiling'}).find_all("dl")[2].get('title')#喜欢
    comment=soup.find(attrs={'class':'data-info d-flex item-tiling'}).find_all("dl")[3].get('title')#评论数量

    node=node.find(attrs={'class': 'grade-box clearfix'}).find_all('dl')
    visit=node[1].dd.get('title')
    jifen=node[2].dd.get('title')
    rank=node[3].get('title')
    print(count,fan,love,comment)
    print(visit,jifen,rank)

    ##专栏个别用户没有专栏
    aside=soup.find(id='asideColumn').ul.find_all('li')
    if len(aside)>0:
       for va in aside:
           title=va.p.a.text
           value=va.select_one('.data').find_all('span')[1].text
           print(title,value)
           print()



if __name__ == "__main__":
    
    url='https://blog.csdn.net/qq_40693171'
    getbaseinfor(url)
