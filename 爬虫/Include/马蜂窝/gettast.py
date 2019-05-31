import re
from bs4 import BeautifulSoup
import requests
import pymysql
# 打开数据库连接
db = pymysql.connect(host="47.100.58.250", user="root",
                     password="123456", db="db", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
pattern = re.compile(r'\d+.html')
def insert(cityid,cityname):
 url='http://www.mafengwo.cn/cy/'+str(cityid)+'/gonglve.html'
 req=requests.get(url=url,headers=header)
 html=req.text
 soup=BeautifulSoup(html,'lxml')
 eatlist=soup.find(attrs={'class':'list-rank'}).find_all('li')
 #具体处理每一条的美食排行
 for food in eatlist:
     foodindex=food.a.get('href')
     foodindex=pattern.search(foodindex).group(0).split('.')[0]
     foodname=food.a.get('title')
     foodimgurl=food.a.img.get('src')
     sql="insert into cityeatrank(name,imgurl,cityname,tastyindex,citynumber)" \
        "values('%s','%s','%s',%d,%d)"%(foodname,foodimgurl,cityname,int(foodindex),int(cityid))
     print(sql)
     try:
         cur.execute(sql)
         db.commit()
     except Exception as e:
         print(e)
         db.rollback()
     print(foodname)
# url1='http://www.mafengwo.cn/cy/10065/gonglve.html'
# url2='http://www.mafengwo.cn/cy/10099/gonglve.html'
# url3='http://www.mafengwo.cn/cy/10208/gonglve.html'
# url4='http://www.mafengwo.cn/cy/10320/gonglve.html'
sql="select city_name,city_province,city_id from citylist"
# try:
#     cur.execute(sql)
#     valueall=cur.fetchall()
#     for value in valueall:
#         print(value[0],value[1],value[2])#不处理直辖市（没数据）
#         # if value[1]=='北京'or value[1]=='上海'or value[1]=='天津'or value[1]=='重庆':
#         #     print('no直辖市')
#         # else:
#         try:
#             insert(value[2],value[0])
#         except Exception as e:
#             print(e)
#
# except Exception as e:
#     print(e)
#     db.rollback()
insert(10065,'北京')
insert(10099,'上海')
insert(10208,'重庆')
insert(10320,'天津')
db.close()



