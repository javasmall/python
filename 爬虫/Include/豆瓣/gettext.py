import requests
from bs4 import BeautifulSoup
import time
import pymysql
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="project", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
def gettext(url):
    req=requests.get(url)
    res=req.text
    soup=BeautifulSoup(res,'lxml')
    commit=soup.select(".short")
    text=''
    for team in commit:
        text+=team.text+' '
    return text
sql="select * from ciyun"
cur.execute(sql)
valuelist=cur.fetchall()
for value in valuelist:
  time.sleep(0.4)
  try:
    name=value[0]
    id=value[2]
    url1="https://movie.douban.com/subject/"+str(id)+"/comments?start=0&limit=20&sort=new_score&status=P"
    url2 = "https://movie.douban.com/subject/" + str(id) + "/comments?start=20&limit=20&sort=new_score&status=P"
    tex1=gettext(url1)
    tex2=gettext(url2)
    tex1+=tex2
    print(1,tex1)
    sql ="update ciyun set text='%s' where id='%s'"%(tex1,id)
    cur.execute(sql)
    db.commit()
  except Exception as e:
      print(e)
gettext("https://movie.douban.com/subject/30228425/comments?status=P")