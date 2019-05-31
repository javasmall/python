import urllib.request as urllib2
import urllib.parse
url = "http://tieba.baidu.com/f"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}

formdata = {
    "ie":"utf-8",
    "kw":"江苏科技大学",
    "fr":"search"
}
data = urllib.parse.urlencode(formdata).encode('utf-8')#要转换成url编码
print(data)
request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)
html=response.read().decode("utf-8")
print( html)