from urllib import request as urllib2
from urllib import parse

url = r'https://movie.douban.com/j/new_search_subjects?'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}
formData = {
    'sort':'T',
    'range':'0,10',
    'tags':'电影,喜剧',
    'start':'0',
}
data = parse.urlencode(formData).encode('utf-8')
request = urllib2.Request(url=url, data=data, headers=headers)
response = urllib2.urlopen(request)
print(response.read().decode("utf-8"))