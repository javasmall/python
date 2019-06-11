import urllib.request as urllib2
import random
proytylist=[
    {"http":"61.135.217.7:80"},
    {"http":"182.38.14.237:8118"},
]
ip=random.choice(proytylist)
httpproxy_handler =urllib2.ProxyHandler(ip)#代理ip的使用

opener=urllib2.build_opener(httpproxy_handler)
request=urllib2.Request('http://www.baidu.com')
res=opener.open(request)
html=res.read().decode()
print(html)