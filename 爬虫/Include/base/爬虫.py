import urllib.request
import bs4
print(bs4)
request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
buff = response.read()
html = buff.decode("utf8")
print(html)