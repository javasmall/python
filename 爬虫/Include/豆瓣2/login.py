import  requests
import urllib.parse
from http import cookiejar

url='https://accounts.douban.com/j/mobile/login/basic'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
        'Origin': 'https://accounts.douban.com',
 'content-Type':'application/x-www-form-urlencoded',
 'x-requested-with':'XMLHttpRequest',
 'accept':'application/json',
 'accept-encoding':'gzip, deflate, br',
 'accept-language':'zh-CN,zh;q=0.9',
 'connection': 'keep-alive'
 ,'Host': 'accounts.douban.com'
 }
data={
    'ck':'',
    'name':'',
    'password':'',
    'remember':'false',
    'ticket':''
}
def login(username,password):
    global  data
    data['name']=username
    data['password']=password
    data=urllib.parse.urlencode(data)
    print(data)
    req=requests.post(url,headers=header,data=data,verify=False)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    print(cookies)
    return cookies
