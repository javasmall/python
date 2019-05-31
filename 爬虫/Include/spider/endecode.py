#编码解吗模块
import urllib.request as urllib2
import urllib.parse
word={"name":"张三"}
word2=urllib.parse.urlencode(word)#编码操作
print(word2)
word3=urllib2.unquote(word2)#解吗操作
print(word3)