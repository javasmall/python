from urllib import request as urllib2
from urllib import parse
from http import cookiejar

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

# 通过cookiejar()类构建一个cookieJar对象，用来保存cookie的值
cookie = cookiejar.CookieJar()

# 通过HTTPCookieProcessor()对象构建一个处理器对象，用来处理cookie
# 参数是CookieJar对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

formData = {
    "email": "mr_mao_hacker@163.com", "password": "alaxxxxxime"
}
data = parse.urlencode(formData).encode('utf-8')
opener = urllib2.build_opener(cookie_handler)

url = 'http://www.renren.com/PLogin.do'

request = urllib2.Request(url=url,data=data ,headers=headers)

response = opener.open(request)
# 打开登陆后的跳转页面
print(response.read().decode())

# 打开个人中心 第二次不用再传表单数据 cookie已经得到了保存
# 第二次可以是get请求，这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
response2 = opener.open('http://www.renren.com/963457938/profile')

print(response2.read().decode())