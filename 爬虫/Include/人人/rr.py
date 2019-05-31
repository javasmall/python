import requests
url='http://120.78.66.11:8080/mybbs/index.action'
i=0
while i<10000000:
    i+=1
    req=requests.get(url)
    print(req)