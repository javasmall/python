import requests
from bs4 import BeautifulSoup
import pymysql
import re
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="car", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
def getcity(shengid,shengname):
   # url2='https://m.mafengwo.cn/mdd/citylist/14387.html#'
    url='http://www.mafengwo.cn/mdd/citylist/'+str(shengid)+'.html#'
    req=requests.get(url=url,headers=header)
    html=req.text
    soup=BeautifulSoup(html,'lxml')
    #找到id
    citylist=soup.find(attrs={'id':'citylistlist'}).find_all('li')
    pattren=re.compile(r'\S+')
    try:
      for city in citylist:
        cityid=city.find(attrs={'class':'img'}).a.get('data-id')
        cityimgurl=city.find(attrs={'class':'img'}).a.img.get('data-original')
        cityname1=city.find(attrs={'class':'img'}).a.div.text
        cityname=pattren.search(cityname1).group(0)
        citydetail1=city.find(attrs={'class':'detail'}).text
        citydetail=pattren.search(citydetail1).group(0)
        #print(cityname,cityid,cityimgurl,citydetail)
        sqlinsert="insert into citylist(city_name,city_province,image_url,city_id,city_detail) " \
                  "values ('%s','%s','%s',%d,'%s')"%(cityname,shengname,cityimgurl,int(cityid),citydetail)
        # try:
        # # 执行sql语句
        #         cur.execute(sqlinsert)
        #         # 提交到数据库执行
        #         db.commit()
        # except:
        #         # 发生错误时回滚
        #         db.rollback()
        print(sqlinsert)
    except Exception as e2:
         print(e2)

# 编写sql 查询语句  user 对应我的表名
sql="select sheng_name,place_id from sheng"
try:
    cur.execute(sql)  # 执行sql语句
    sqlvalue=cur.fetchall()
    for sheng in sqlvalue:
        print(sheng[0], sheng[1])
        getcity(sheng[1],sheng[0])
except Exception as e:
    print(e)
finally:
    db.close()  # 关闭连接
#getcity(5,5)