from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print(driver.title)


import time
import requests
 
from selenium import webdriver
from bs4 import BeautifulSoup
 
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
headers = {'User-Agent': user_agent}
#事先在百度输入框中搜索要下载的图片，取出链接地址。这里搜索的是"证件照"
httpUrl = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1526001481384_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E7%99%BB%E8%AE%B0%E7%85%A7"
 
 
def main():
    driver = webdriver.Chrome()
    driver.get(httpUrl)
 
    soup = BeautifulSoup(driver.page_source, "html.parser")
    imglist = soup.find_all("img", {'class': 'main_img img-hover'})  # 内容
    x = 0
    for img in imglist:
        print(img['data-imgurl'])
        saveImg(img['data-imgurl'], x)
        x += 1
    driver.close()
 
 
def saveImg(pic_link, x):
    path = "img/"  # 存储路径
    pp = requests.get(pic_link, headers=headers)
    pth = path + str(x) + ".png"  # 设置图片名
    with open(pth, "wb") as f:
        for chunk in pp:  # 读取每个图片链接的二进制数据
            f.write(chunk)  # 写入
    print("第%s张下载好" % x)
 
if __name__ == '__main__':
    main()