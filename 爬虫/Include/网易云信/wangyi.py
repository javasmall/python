import requests
import random
import time
import threading
from queue import Queue
def loadip():
    url2 = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=f16367295e284173ae450fc38d9098b3&count=20&expiryDate=0&format=1&newLine=2'
    req = requests.get(url2)
    date = req.json()
    if(date['code'])!='3001':
        ipdate2 = date['msg']
        global ipdate
        ipdate.extend(ipdate2)
        for va in ipdate2:
          que.put(va)
        print(ipdate)

class downspider(threading.Thread):
    def __init__(self, threadname, que):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.que = que

    def run(self):
        print('start thread' + self.threadname)
        while True:
            try:
                print(self.name,end='')
                toupiaospider(que,self.threadname)
            except Exception as e:
                print(e,'888')
                break
def getproxies():
    b = ipdate[0]
    b=que.get()
    d = '%s:%s' % (b['ip'], b['port'])
    global proxies
    proxies['http'] = d
    global msg
    msg = b
    return proxies
def toupiaospider(que,threadname):
    if (que.qsize() < 15):  # 拓展ip池
        loadip()
    proxies2=getproxies()
    for i in range(0,5):
        try:
            #formData['times']=i
            req = requests.post(url, headers=header, data=formData, proxies=proxies2, timeout=1.5)
            res = req.json()
            if res['res']==2001 or req.status_code!=200:
                #ipdate.remove(msg)
                 continue
            print(threadname,res,que.qsize())
        except Exception as e:
            print('errror',e)
            # ipdate.remove(msg)

if __name__ == '__main__':
    ipdate = []
    msg = {}
    proxies = {'http': ''}
    stadus = 0
    que = Queue()
    threads=[]#线程
    url='http://yunxin.163.com/api/vote/update'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    formData = {
        'Referer':'http://yunxin.163.com/promotion/minichallenge/gallery?from=groupmessage&isappinstalled=0',
        'id':'17',
        'times':'1',
        'activity':'minichallenge1'
    }
    proxies = {'http': '182.247.92.99:21136',
               }
    loadip()
    time.sleep(5)
    threadList = ['thread-1','thread-2','thread-3','thread-4','thread-4']
    for j in threadList:
        thread = downspider(j, que)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    # for i in range(100):
    #     try:
    #         toupiaospider()
    #     except Exception as e:
    #         print('error')
    #         try:
    #             ipdate.remove(msg)
    #         except Exception as e2:
    #             print("e2",e2)
