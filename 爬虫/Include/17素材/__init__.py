import  requests

url='https://www.17sucai.com/preview/1750622/2019-09-22/growth/index.html'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
 }
req=requests.get(url,verify=False)
print(req.text)