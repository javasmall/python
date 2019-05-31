#get请求
import urllib.request as urllib2
import  urllib.parse
url='http://www.baidu.com/s'
word={'wd':'江苏科技大学'}
word=urllib.parse.urlencode(word)#进行编码处理

newurl=url+'?'+word
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}#请求头
request=urllib2.Request(newurl,headers=header)
res=urllib2.urlopen(request)
html=res.read()

print(html.decode('utf-8'))