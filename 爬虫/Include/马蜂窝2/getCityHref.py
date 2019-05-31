import requests
from bs4 import BeautifulSoup
import pymysql
import re
import json
import time
import random
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="date", port=3306)
ipdate=[]
msg={}
proxies = {'http': ''}
stadus=0
def loadip():
   url='http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=14b5feb7445241329a1381e26e1f6aa7&count=20&expiryDate=0&format=1&newLine=2'
   req=requests.get(url)
   date=req.json()
   ipdate2=date['msg']
   global ipdate
   ipdate.extend(ipdate2)
   print(ipdate)
def getproxies():
    b=random.choice(ipdate)
    d = '%s:%s' % (b['ip'], b['port'])
    global proxies
    proxies['http']=d
    global msg
    msg=b
# 使用cursor()方法获取操作游标
cur = db.cursor()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

def jud(cityid):
   try:
    url='http://www.mafengwo.cn/travel-scenic-spot/mafengwo/'+str(cityid)+'.html'
    if(len(ipdate)<30):#拓展ip池

        loadip()
    getproxies()
    req=requests.get(url,headers=header,proxies=proxies,timeout=2,allow_redirects=False)
    global stadus
    stadus=req.status_code
    print(cityid,stadus)
    if stadus==200:#请求成功
        html=req.text
        soup=BeautifulSoup(html,'lxml')
        href=soup.find(attrs={'class':'navbar clearfix'})
        infourl='http://www.mafengwo.cn'+str(href.find(attrs={'data-cs-p':'概况'}).get('href'))#主要信息
        viewhref='http://www.mafengwo.cn'+str(href.find(attrs={'data-cs-p':'景点'}).get('href'))#景点信息
        foodhref='http://www.mafengwo.cn'+str(href.find(attrs={'data-cs-p':'餐饮'}).get('href'))#餐饮信息'
        updatehref="update cityhref set infohref='%s',viewhref='%s',foodhref='%s' where city_id=%d"%(infourl,viewhref,foodhref,cityid)
        print(cityid,foodhref,len(ipdate))
        try:
            cur.execute(updatehref)
            db.commit()
        except Exception as e:
            print(updatehref,e)
            db.rollback()
        stadus=0
   except Exception as e3:
       if ( stadus == 301 or stadus==302 or stadus==200):
           print('no prbo',cityid,stadus)
       else:
         print(e3, cityid, stadus)
         try:
             print('remove')
             ipdate.remove(msg)
         #   ipdate.remove(msg)
         except Exception as  e6:
             print(e6)
         jud(cityid)

loadip()#先填充一部分ip
time.sleep(5)#休眠五秒
sql='select city_id,infohref from cityhref'
cur.execute(sql)
value=cur.fetchall()
# for cityid in value:
#     if(cityid[1]==None):
#         print('start:',cityid[0])
#         jud(cityid[0])
#jud(64641)
# jud(5429475)
db.close()