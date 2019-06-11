import requests
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# kw = {'wd':'长城'}
# res=requests.get('http://www.baidu.com',params=kw,headers=headers)
#print(res.text)
# print(res.content)
# print(res.encoding)
# print(res.status_code)
# print(res.url)

url = "http://www.overlove.xin:8080/test/getmoviebytype"
userangert = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
header = {'User-Agent': userangert}
req = requests.get(url, headers=header)
#乱码问题的解决方案油两个
# req.encoding='gbk'
json=req.json()
print(json)
horror=json['horror']
print(horror)
a1=horror[1]
print(a1)
id=a1['id']
print(id)

#html = req.content#contenet是流内容，可以获得图片等信息。
#print(html.decode('gbk'))