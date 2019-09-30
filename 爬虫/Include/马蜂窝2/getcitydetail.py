import requests
import pymysql
import random
import time
import re
from bs4 import BeautifulSoup
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

db = pymysql.connect(host="127.0.0.1", user="root",
                     password="123456", db="date", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
ipdate = []
msg = {}
proxies = {'http': ''}
stadus = 0


def loadip():
    url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=14b5feb7445241329a1381e26e1f6aa7&count=10&expiryDate=0&format=1&newLine=2'
    req = requests.get(url)
    date = req.json()
    ipdate2 = date['msg']
    global ipdate
    if date['code']==0:
       ipdate.extend(ipdate2)
       print(ipdate)
    else:
        print('增加失败')

def getproxies():
    b = random.choice(ipdate)
    d = '%s:%s' % (b['ip'], b['port'])
    global proxies
    proxies['http'] = d
    global msg
    msg = b
# 获取详细信息
def getdetail(url, cityid):
    global stadus
    global msg
    try:
        if (len(ipdate) < 8):  # 拓展ip池
            loadip()
        getproxies()
        req = requests.get(url, headers=header, proxies=proxies, timeout=2, allow_redirects=False)
        stadus = req.status_code
        print(cityid, stadus, len(ipdate))
        if stadus == 200:  # 请求成功
            html = req.text
            soup = BeautifulSoup(html, "lxml")
            first = soup.select(".part")
            detail = ['', '', '', '', '', '', '', '', '', '']
            index = 0
            for value in first:
                detail[index] = value.text.replace(" ", "")
                index = index + 1
            sql2 = "update citydetail set city_information='%s' ,detail1='%s', detail2='%s', detail3='%s' where city_id=%d" % (
                detail[0], detail[1], detail[2], detail[3], cityid)
            # try:
            #     cur.execute(sql2)
            #     db.commit()
            # except Exception as e3:
            #     db.rollback()
            #     print(e3,'sql错误')
            stadus = 0
    except Exception as e6:
        if (stadus == 301 or stadus == 302 or stadus == 200):
            print('no prbo', cityid, stadus)
        else:
            print(e6, cityid, stadus)
            try:
                print('remove', ipdate, msg)
                ipdate.remove(msg)
            except Exception as  e7:
                print(e7, '删除失败')
            getdetail(url, cityid)


def getviewdetail(viewname, id, cityid, cityname):
    global stadus
    global msg
    try:
        if len(ipdate) < 25:  # 拓展ip池
            loadip()
        getproxies()
        url = 'http://www.mafengwo.cn/poi/' + str(id) + '.html'
        req = requests.get(url, headers=header, proxies=proxies, timeout=2, allow_redirects=False)
        stadus = req.status_code
        if stadus == 200:
            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            imgurl = soup.select_one(".pic-big").img.get('src')  # 图片的信息
            viewsummuty = soup.select_one(".summary").text.replace(' ', '')
            sqlsert = "insert into cityview (city_id,cityname,viewname,viewimg,viewid,viewdetail)" \
                      "values('%s','%s','%s','%s','%s','%s')" % (
                          int(cityid), cityname, viewname, imgurl, int(id), viewsummuty)
            try:
                cur.execute(sqlsert)
                db.commit()
            except Exception as  e:
                print(e)
                db.rollback()
            stadus=0
    except Exception as e7:
        if (stadus == 301 or stadus == 302 or stadus==200):
            print('wrong', id, cityid, stadus, cityname)
        else:
            print(e7, cityid, stadus,len(ipdate))
            try:
                print('remove', ipdate, msg)
                ipdate.remove(msg)
            except Exception as  e8:
                print(e8, '删除失败')
            getviewdetail(viewname, id, cityid, cityname)


pattern = re.compile(r'\d+')
def getview(url, cityid, cityname):
    global stadus
    global msg
    try:
        if (len(ipdate) < 25):  # 拓展ip池
            loadip()
        getproxies()
        req = requests.get(url, headers=header, proxies=proxies, timeout=2, allow_redirects=False)
        stadus = req.status_code
        if (stadus == 200):

            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            viewlist = soup.find_all(attrs={'class': 'item clearfix'})
            for view in viewlist:
                viewname = view.a.get('title')
                viewhref = view.a.get('href')
                viewid = pattern.search(viewhref).group(0)
                print(viewid)
                getviewdetail(viewname, viewid, cityid, cityname)
            stadus=0
    except Exception as e7:
        if (stadus == 301 or stadus == 302 or stadus==200):
            print(e7, 'no prbo', cityid, stadus, cityname)
        else:
            print(e7, cityid, stadus,len(ipdate))
            try:
                print('remove', ipdate, msg)
                ipdate.remove(msg)
            except Exception as  e8:
                print(e8, '删除失败')
            getview(url, cityid, cityname)


# # 进入概况
# def savaimg(imgurl, cityid):
#     req = requests.get(imgurl, headers=header)
#     html = req.text
#     soup = BeautifulSoup(html, 'lxml')
#     imgurlbig = soup.find(attrs={'class': 'pic-big'}).img.get('src')
#     sql3 = "update citylist set image_url2='%s' where city_id=%d" % (imgurlbig, cityid)
#     # try:
#     #     cur.execute(sql3)
#     #     db.commit()
#     # except Exception  as e4:
#     #     print(e4)
#     # time.sleep(2.9)
#     print(imgurlbig)
#
#
def getimgurl( cityid):
   try:
    url='http://www.mafengwo.cn/mdd/ajax_photolist.php'
    data={'act':'getMddPhotoList',
          'mddid': cityid,
          'page': '1'}
    data=urllib.parse.urlencode(data)
    url=url+'?'+data
    req = requests.get(url, headers=header,timeout=1.5)
    html = req.text
    soup = BeautifulSoup(html, "lxml")
    link=soup.select(".col3")
    imgsrc=['','','','']
    imgsrc[0]=link[0].a.img.get('src')
    imgsrc[1] = link[1].a.img.get('src')
    imgsrc[2] = link[2].a.img.get('src')
    sqlupdate="update citydetail set bigimg='%s',bigimg2='%s',bigimg3='%s'where city_id=%d"%(str(imgsrc[0]),str(imgsrc[1]),str(imgsrc[2]),cityid)
    cur.execute(sqlupdate)
    db.commit()
    print(cityid)
   except Exception as e:
       print(e)

if __name__ == '__main__':
    # 编写sql 查询语句  user 对应我的表名
    # getdetail("http://www.mafengwo.cn/baike/info-11319.html", int(11319))

    sql = 'select city_id from citydetail'
    cur.execute(sql)
    value = cur.fetchall()
    b=False
    for q in value:
        if(q[0]==63870):
            b=True
        if b==True:
           getimgurl(q[0])
    # print(value[5][1],value[5][0])
    # getview('http://www.mafengwo.cn/jd/13380/gonglve.html', 13380, '门头沟')
    # for q in value:
    #     print(q[2],b)
    #     if q[2]=='运城':
    #         b=True
    #         loadip()
    #         time.sleep(5)
    #         loadip()
    #         time.sleep(5)
    #     if b==True:
    #        getview(q[1],q[0],q[2])
    # with ThreadPoolExecutor(2) as executor:
    #     for q in value:
    #         print(q[1], q[0])
    #         executor.submit(getview, q[1], int(q[0]), q[2])
    #getimgurl(10065)
    db.close()
