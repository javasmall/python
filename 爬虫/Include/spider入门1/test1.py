# -*- coding:utf-8 -*-
import urllib.request as urllib2
header={"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request = urllib2.Request('http://www.baidu.com',headers=header)
response = urllib2.urlopen(request)
buff = response.read()
html = buff.decode()
print(html)

