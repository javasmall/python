import requests
from bs4 import BeautifulSoup
import pymysql
import time
db = pymysql.connect(host="biggsai.com", user="root",
                     password="123456", db="project", port=3306)
#使用cursor()方法获取操作游标
cur = db.cursor()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

url1="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=100"
req=requests.get(url=url1)
res=req.json()
a=res['subjects']
def judmovie(url,name,imgurl,id):
    req=requests.get(url,headers=header)
    res=req.text
    soup=BeautifulSoup(res,"lxml")
    timelong=soup.find(attrs={'property':'v:runtime'}).text
    timelong=str(timelong).replace('分钟','')
    introduction = soup.find(attrs={'property': 'v:summary'}).text
    introduction = str(introduction).replace(' ', '')
    print(timelong,introduction)
    sql="insert into movie(name,type,time_long,description,img)values('%s','action','%d','%s','%s')"%(name,int(timelong),introduction,imgurl)
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    sql2="insert into ciyun(moviename,id)values('%s','%s')"%(name,id)
    try:
        cur.execute(sql2)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


for team in a:
    #print(team)
    id=team['id']
    img=team['cover']
    url=team['url']
    name=str(team['title']).replace(' ','')
    print(id,name,img,url)
    try:
     judmovie(url,name,img,id)
     time.sleep(1)
    except Exception as  e:
        print(e)

#judmovie("https://movie.douban.com/subject/30228425/?tag=%E6%81%90%E6%80%96&from=gaia",'fds','jj')