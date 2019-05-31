import re
from bs4 import BeautifulSoup
import requests
import pymysql
import threading
from queue import Queue
import time
import random
import requests.exceptions

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root",
                     password="123456", db="date", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
threads = []
que = Queue()
ipdate = []
# msg = {}

proxies = {'http': ''}

header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45"}
threadlock=threading.Lock()

def loadip():
    url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=8d9213f4da15491cab3c76544b404727&count=12&expiryDate=0&format=1&newLine=2'
    req = requests.get(url)
    date = req.json()
    ipdate2 = date['msg']
    global ipdate
    print(date['code'])
    if int(date['code']) == 0:
        ipdate.extend(ipdate2)
        print(ipdate)
    else:
        print('增加失败')


def getproxies():
    b = random.choice(ipdate)
    d = '%s:%s' % (b['ip'], b['port'])
    global proxies
    proxies['http'] = d
    return b


class downspider(threading.Thread):
    def __init__(self, threadname, que):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.que = que

    def run(self):
        print('start thread' + self.threadname)
        while True:
            try:
                crawl(self.name, self.que)
            except Exception as e:
                print(e,'888')
                break
def savaimg(foodhref, name, cityid, cityname, smallimg, foodid):
        if (len(ipdate) < 30):  # 拓展ip池
            loadip()
        msg2 = getproxies()
        req = requests.get(foodhref, headers=header, proxies=proxies, timeout=2)
        status = req.status_code
        try:
            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            bigimg = soup.select(".img-con")[0].img.get('src')
            fooddetail = soup.select(".m-txt")[0].text.replace(' ', '')
            sqlinsert = "insert into foodtest (name,imgurl,cityname,foodid,cityid,fooddetail,imglogo)" \
                        "values('%s','%s','%s',%d,%d,'%s','%s')" % (
                        name, bigimg, cityname, int(foodid), int(cityid), fooddetail, smallimg)
            try:
                cur.execute(sqlinsert)
                db.commit()
            except:
                db.rollback()
        except requests.exceptions.ConnectTimeout :
            print('timeout', status)
            try:
                 ipdate.remove(msg2)
            except Exception as e6:
                 print(e6,ipdate,msg2)
            savaimg(foodhref, name, cityid, cityname, smallimg, foodid)
        except:
            if(status!=200):
                try:
                    ipdate.remove(msg2)
                except Exception as e6:
                    print(e6, ipdate, msg2)
                savaimg(foodhref, name, cityid, cityname, smallimg, foodid)
def parse(url, cityid, cityname, threadname):
        if (len(ipdate) < 15):  # 拓展ip池
            loadip()
        msg=getproxies()
        req = requests.get(url, headers=header, proxies=proxies, timeout=2)
        status = req.status_code
        try:
            print(threadname,cityid, status, cityname,url,len(ipdate))

            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            foodrank = soup.select(".list-rank")
            foodlist = soup.find_all('li', attrs={'class': re.compile('rank-item+')})
            pattern = re.compile(r'\d+.html')
            pattern2 = re.compile(r'\d+')
            for j in foodlist:
                name = j.a.get('title')
                smallimg = j.a.span.img.get('src')
                foodhref = 'http://www.mafengwo.cn' + str(j.a.get('href'))
                foodindex2 = pattern.search(foodhref).group(0)
                foodid = pattern2.search(str(foodindex2)).group(0)
                print(foodid, foodhref, name, cityid, smallimg)
                savaimg(foodhref, name, cityid, cityname, smallimg, foodid)
                # sqlinsert = "insert into cityfood (name,cityname,foodid,cityid,imglogo)" \
                #             "values('%s','%s',%d,%d,'%s')" % (
                #                 name,  cityname, int(foodid), int(cityid), smallimg)
                # cur.execute(sqlinsert)
                # db.commit()
        except requests.exceptions.ConnectTimeout as e7:
            print(e7,'errer')
            try:
               ipdate.remove(msg)
               print('remove',msg,ipdate)
            except Exception as e6:
               print(e6, ipdate, msg)
            parse(url, cityid, cityname, threadname)
        except Exception as  e9:
            print('status:',status,e9)
            if(status!=200):
             try:
                 print('remove', msg, ipdate)
                 ipdate.remove(msg)
             except Exception as e6:
                 print(e6,ipdate,msg)
             parse(url, cityid, cityname, threadname)




def crawl(threadname, que):
        node = que.get(timeout=0.5)

        url = node['url']
        cityid = node['cityid']
        cityname = node['cityname']
        parse(url, cityid, cityname, threadname)

def main():
    threadList = ['thread-1']
    sql = 'select city_id,foodhref,city_name from city_href '
    cur.execute(sql)
    value = cur.fetchall()
    for q in value:
        #parse(q[1],q[0],q[2],'test')
        node = {'url': q[1], 'cityid': q[0], 'cityname': q[2]}
        que.put(node)
    for j in threadList:
        thread = downspider(j, que)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    db.close()


if __name__ == '__main__':
    loadip()
    time.sleep(5)
    main()
    # parse('http://www.mafengwo.cn/cy/10024/gonglve.html',10024,'宿迁','thread6')
    # savaimg('http://www.mafengwo.cn/cy/10024/2906.html','血粑鸭',10024,'宿迁','222',2906)
