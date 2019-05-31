import  requests
from bs4 import BeautifulSoup
import random
header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45"}

proxies = {
           }
url2="http://www.mafengwo.cn/cy/13380/gonglve.html"
req=requests.post(url2,headers=header)
print(req.status_code)