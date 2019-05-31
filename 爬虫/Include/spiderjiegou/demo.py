from bs4 import BeautifulSoup


import urllib.request

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html, "html5lib")
# 这需要安装html5lib模块
text = soup.get_text(strip=True)
print(text)