import urllib.request as urllib2
httphander=urllib2.HTTPHandler()
#支持处理http请求
opener=urllib2.build_opener(httphander)# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
request=urllib2.Request('http://www.baidu.com')
res=opener.open(request)
print(res.read().decode('utf-8'))