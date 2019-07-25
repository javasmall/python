import requests
from bs4 import BeautifulSoup

url='https://passport.csdn.net/v1/register/pc/login/doLogin'
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
data='{"loginType":"1","pwdOrVerifyCode":"你的密码",' \
 '"userIdentification":"你的账号","uaToken":"",' \
 '"webUmidToken":""}'
req=requests.post(url,data=data,headers=header)
cookies = requests.utils.dict_from_cookiejar(req.cookies)
res=req.text
print(res)
print(req.status_code)
print(cookies)

url2='https://blog.csdn.net/nav/watchers'
req2=requests.get(url2,cookies=cookies)
soup=BeautifulSoup(req2.text,'lxml')

print(soup.text)
