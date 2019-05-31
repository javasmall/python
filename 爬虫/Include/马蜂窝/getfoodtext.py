import re
from bs4 import BeautifulSoup
import requests
import pymysql
# 打开数据库连接
db = pymysql.connect(host="47.100.58.250", user="root",
                     password="123456", db="db", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
sql="select citynumber,tastyindex from cityeatrank where citynumber in(10065,10099,10208,10320)"
cur.execute(sql)
value=cur.fetchall()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
for number in value:
   try:
    print(number[0],number[1])
    url='http://www.mafengwo.cn/cy/'+str(number[0])+'/'+str(number[1])+'.html'
    res=requests.get(url=url,headers=header)
    html=res.text
    soup=BeautifulSoup(html,'lxml')
    text=soup.find(attrs={'class':'m-txt'}).p.text
    imgurl=soup.find(attrs={'class':'img-con'}).img.get('src')
    sqlinsert="update cityeatrank set imgurl='%s',fooddetail='%s' where tastyindex=%d"%(imgurl,text,int(number[1]))
    print(text)
   #  try:
   #      cur.execute(sqlinsert)
   #      db.commit()
   #  except Exception as e:
   #      print(e)
   #      db.commit()
   #  print(imgurl)
   except Exception as e2:
       print(e2)
db.close()
