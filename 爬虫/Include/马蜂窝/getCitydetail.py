import  requests
import  pymysql
import random
import time
from  bs4 import  BeautifulSoup

db = pymysql.connect(host="47.100.58.250", user="root",
                     password="123456", db="db", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()
# 编写sql 查询语句  user 对应我的表名
user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Connection': 'close',
        }
proxies = {'http': '221.6.201.18:9999',
           'https':'221.6.201.18:9999'
           }
#获取详细信息
def getdetail(url,cityid):
    req=requests.get(url,headers=header)
    html=req.text
    soup=BeautifulSoup(html,"lxml")
    first=soup.select(".part")
    firstvalue=first[0].text.replace("\n"," ")
    secondvalue=first[1].text.replace("\n"," ")
    sql2="update citylist set city_information='%s' ,best_time='%s' where city_id=%d"%(firstvalue,secondvalue,cityid)
    try:
        cur.execute(sql2)
        db.commit()
    except Exception as e3:
        print(e3)
    print(sql2)
    print(secondvalue)
    time.sleep(1.2)
#进入概况
def getdetailurl(url,cityid):
    #proty=random.choice(proxies)
    req=requests.get(url,headers=header)
    html=req.text
    soup=BeautifulSoup(html,"lxml")
    firsturl=soup.find(attrs={'class':'navbar-btn'})
    href=firsturl.get('href')
    href="http://www.mafengwo.cn"+href
    print(href)
    time.sleep(1.2)
    getdetail(href,cityid)
def savaimg(imgurl,cityid):
    req=requests.get(imgurl,headers=header)
    html=req.text
    soup=BeautifulSoup(html,'lxml')
    imgurlbig=soup.find(attrs={'class':'pic-big'}).img.get('src')
    sql3 = "update citylist set image_url2='%s' where city_id=%d" % (imgurlbig, cityid)
    try:
        cur.execute(sql3)
        db.commit()
    except Exception  as e4:
        print(e4)
    time.sleep(2.9)
    print(imgurlbig)

def getimgurl(url,cityid):
    req=requests.get(url,headers=header)
    html=req.text
    soup=BeautifulSoup(html,"lxml")
    imghref1=soup.select('.pic')[1].a.get('href')
    img1url='http://www.mafengwo.cn'+imghref1
    time.sleep(2.9)
    try:
        savaimg(img1url,cityid)
    except Exception as e8:
        print(e8)
sql="select city_id from citylist"
try:
    cur.execute(sql)
    value=cur.fetchall()
    time1=0
    for q in value:
        print(q[0])
        # url="http://www.mafengwo.cn/travel-scenic-spot/mafengwo/"+str(q[0])+".html"#获取一些介绍
        # print(url)
        # try:
        #     getdetailurl(url,q[0])
        # except Exception as e2:
        #     print(e2)
        time1+=1;
        url="http://www.mafengwo.cn/jd/"+str(q[0])+"/gonglve.html"
        print(url)
        # if(time1>40):
        #  try:
        #    getimgurl(url,int(q[0]))
        #  except Exception as e5:
        #     print(e5)
except Exception as e:
    print(e)
#getdetailurl("http://www.mafengwo.cn/travel-scenic-spot/mafengwo/12672.html",int(12672))
#getimgurl("http://www.mafengwo.cn/jd/10651/gonglve.html",10651)
db.close()
