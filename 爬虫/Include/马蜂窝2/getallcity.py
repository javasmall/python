import requests
from bs4 import BeautifulSoup
import pymysql
import re
import json
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="date", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
def getcitylist(shengid,shengname):
    # url2='https://m.mafengwo.cn/mdd/citylist/14387.html#'
    url='http://www.mafengwo.cn/mdd/citylist/'+str(shengid)+'.html#'
    req=requests.get(url=url,headers=header)
    html=req.text
    soup=BeautifulSoup(html,'lxml')
    #找到页数
    count=soup.select(".count")[0].text
    pattren=re.compile(r'[0-9]+')
    count=pattren.search(count).group(0)
    count=int(count)+1
    print(count)
    for i in range(1,count):
       getajax(shengid,i,shengname)
def getajax(shengid,index,shengname):
    url='http://www.mafengwo.cn/mdd/基础知识/list/pagedata_citylist'
    date={'mddid':shengid,'page':index}
    req=requests.post(url,headers=header,data=date)
    #req.encoding='unicode_escape'
    html=req.text
    #html=html.decode('unicode_escape')
    q=json.loads(html)
    #print(q)
    html=q['list']
    #print(html)
    soup=BeautifulSoup(html,'lxml')
    citylist=soup.select('.item')
    pattren = re.compile(r'\S+')
    for city in citylist:
        cityid=city.div.a.get('data-id')
        cityhref='http://www.mafengwo.cn/'+city.div.a.get('href')
        cityname=city.find(attrs={'class':'title'}).text
        chinesename=pattren.search(cityname).group(0)
        citydetail=city.select('.detail')[0].text.replace(' ','').replace('\n','')
        cityimg=city.select('.img')[0].a.img.get('data-original')
        print(cityname)
        sqlinsert = "insert into cityhref_copy(city_name,city_province,image_url,city_id,city_detail) " \
                    "values ('%s','%s','%s',%d,'%s')" % (chinesename,shengname,cityimg, int(cityid), citydetail)
        try:
        # 执行sql语句
                cur.execute(sqlinsert)
                # 提交到数据库执行
                db.commit()
        except:
                # 发生错误时回滚
                db.rollback()
#编写sql 查询语句  user 对应我的表名
# sql="select sheng_name,place_id from sheng"
# try:
#     cur.execute(sql)  # 执行sql语句
#     sqlvalue=cur.fetchall()
#     for sheng in sqlvalue:
#         print(sheng[0], sheng[1])
#         getcitylist(sheng[1],sheng[0])
# except Exception as e:
#     print(e)
# finally:
#     db.close()  # 关闭连接
db.close()
#getcity(5,5)