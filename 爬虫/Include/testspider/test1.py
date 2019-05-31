import requests
from http import cookiejar
formData = {
    'username':162210702234,
    'password':'bigsai',
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
url="http://biggsai.com/volunteer/login"
req=requests.post(url,data=formData)
cookies = requests.utils.dict_from_cookiejar(req.cookies)
print(cookies)
for key in cookies.keys():
    print(key,cookies.get(key))
print(req.text)

url2="http://biggsai.com/volunteer/public/getallcampus"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
req2=requests.get(url2,cookies=cookies)
print(req2.text)


