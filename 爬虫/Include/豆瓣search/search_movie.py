import  requests
from bs4 import BeautifulSoup
url="https://movie.douban.com/subject_search?search_text=%E7%81%B5%E9%AD%82%E6%91%86%E6%B8%A1&cat=1002"
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
req=requests.get(url,headers=header)
soup=BeautifulSoup(req.text,'lxml')
print(soup.text)