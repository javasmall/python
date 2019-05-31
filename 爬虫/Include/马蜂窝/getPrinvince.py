#爬去入口网页。从入口处获取省份和城市的名称
#
import requests
from bs4 import BeautifulSoup
import re
import pymysql
#筛选数据插入mysql,连接数据库
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456", db="car", port=3306)
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
# def insert(sql):
#     try:
#         # 执行sql语句
#         cur.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 发生错误时回滚
#         db.rollback()
URL="http://www.mafengwo.cn"
url="http://www.mafengwo.cn/mdd"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
req=requests.get(url=url,headers=header)
#print(req.content.decode())
html=req.content.decode()
soup=BeautifulSoup(html,'html.parser')
soup1=soup.find_all('div',attrs={'class':'hot-list clearfix'})[0]#只有一个对象
city=soup1.find('dd').find_all('a')#已经处理好，dd tag是城市，dt是省份，第一个dd就是直辖市。我们需要的
sheng=soup1.select('dt')#<dt>....</dt>
pattern=re.compile(r'\d+.html')
pattern2=re.compile(r'\d+')
for city1 in city:
    cityurl=URL+city1.get('href')
    cityname=city1.text
    cityidpattern=pattern.search(cityurl).group(0)#10065.html
    cityid=pattern2.search(cityidpattern).group(0)#10065
    #sql="insert into sheng(sheng_name,sheng_url,place_id) values('%s','%s',%d)"%(cityname,cityurl,int(cityid))
    #插入数据库
    #insert(sql)
    print('%s  %s %s'%(cityname,cityurl,cityid))#北京  http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10065.html需要提取10065
for sheng1 in sheng:
    if sheng1.text!='直辖市':#过滤掉直辖市
        for sheng2 in sheng1.find_all('a'):
            shengurl=URL+sheng2.get('href')
            shengname=sheng2.text
            shengidpattern=pattern.search(shengurl).group(0)
            shengid=pattern2.search(shengidpattern).group(0)
            #sql = "insert into sheng(sheng_name,sheng_url,place_id) values('%s','%s',%d)" % (shengname, shengurl, int(shengid))
            #insert(sql)
            print('%s  %s  %s' % (shengname, shengurl,shengid))
