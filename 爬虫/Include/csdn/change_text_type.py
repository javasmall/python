import  requests
from bs4 import BeautifulSoup
import json
import threading
from queue import Queue
queue= Queue()
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer':'https://passport.csdn.net/login',
        'origin':'https://passport.csdn.net',
        'content-Type':'application/json;charset=UTF-8',
        'x-requested-with':'XMLHttpRequest',
        'accept':'application/json, text/plain, */*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
         'connection': 'keep-alive'
         ,'Host': 'passport.csdn.net'
        }
data={"loginType":"1","pwdOrVerifyCode":"",' \
     '"userIdentification":"","uaToken":"",' \
     '"webUmidToken":""}
cookies=""
type='public'
## 登录
def login(usename,password):
    global cookies
    global data
    loginurl = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
    data['userIdentification']=usename
    data['pwdOrVerifyCode']=password
    data=str(data)
    print(data)
    req = requests.post(loginurl, data=data, headers=header)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    res = req.text
    print(req.status_code)
    print(cookies)
    url="https://blog.csdn.net/"+str(cookies['UN'])
    return url
#将url文章添加到queue
def addurl(url):
    req2 = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(req2.text, 'lxml')
    ##获取页数
    pagetotal = soup.select(".text-center")[0].get("title")
    pagetotal = (int)(((int)(pagetotal) + 19) / 20);
    print(pagetotal)
    for index in range(pagetotal):
        url2 = url+"/article/list/" + str(index + 1)
        print(url2)
        req = requests.get(url2, cookies=cookies)
        soup = BeautifulSoup(req.text, 'lxml')
        pages = soup.find(id='mainBox').find_all(attrs={'class': 'article-item-box'})
        for page in pages:
            try:
                href = page.find("a").get("href")
                id = href.split("/")
                id = id[len(id) - 1]
                print(href, id)
                queue.put(id)
            except Exception as e:
                print(e)
def addurl_by_type(url):
    req2 = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(req2.text, 'lxml')
    ##获取页数
    pagetotal = soup.select(".text-center")[0].get("title")
    pagetotal = (int)(((int)(pagetotal) + 19) / 20);
    print(pagetotal)
    for index in range(pagetotal):
        url2 = url + "/" + str(index + 1)+"?"
        print(url2)
        req = requests.get(url2, cookies=cookies)
        soup = BeautifulSoup(req.text, 'lxml')
        pages = soup.find(id='mainBox').find_all(attrs={'class': 'article-item-box'})
        for page in pages:
            try:
                href = page.find("a").get("href")
                id = href.split("/")
                id = id[len(id) - 1]
                print(href, id)
                queue.put(id)
            except Exception as e:
                print(e)

def change(id):
    global read_needType
    url3 = "https://mp.csdn.net/mdeditor/" + str(id) + "#"
    # req = requests.get(url3, cookies=cookies)
    url = "https://mp.csdn.net/mdeditor/getArticle?id=" + str(id)
    req = requests.get(url, cookies=cookies)
    res = req.json()
    data = res['data']
    print(res)
    data['readType'] = read_needType
    #print(data['readType'])

    url = "https://mp.csdn.net/mdeditor/saveArticle"
    req = requests.post(url, cookies=cookies, data=data)
    res = req.text
    #print(res)

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
                id=queue.get()
                change(id)
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    url=""
    threads=[]
    read_needType=['public','read_need_fans','read_need_vip']
    name=input("name:")
    password=input("password:")
    print("type:\n1:全部可看 \n2关注可看 \n3vip会员可看")
    value=input("请输入数字")
    value=int(value)-1
    read_needType=read_needType[value]
    print("type:\n1:全部更改 \n2更改一个分类")
    all_or_type=input("输入更改范围(数字)")
    all_or_type=int(all_or_type)

    if all_or_type==1:
        url=login(name,password)
        addurl(url)
    else:
        print("输入分类首页url：")
        url=input("url:")
        login(name,password)
        addurl_by_type(url)
    print(url)

    threadList = ['thread-1', 'thread-2', 'thread-3', 'thread-4', 'thread-5']
    for j in threadList:
        thread = downspider(j, queue)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()

