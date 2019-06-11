import requests
import re
class spider:
    def loadpage(self,page):
        url = "https://www.neihan8.com/article/list_5_"+str(page)+".html"
        userangert = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        header = {'User-Agent': userangert}
        req = requests.get(url, headers=header)
        req.encoding='gbk'
        html = req.text
       # print(html)
        patten=re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        list=patten.findall(html)

        return list

    def writetofile(self, text,myfile):

        myfile.write(text)
        myfile.write('---------------------------------------------------')

    def printonepage(self,page,list):
        print("第%d页爬取完毕"%page)
        for str in list:
            str=str.replace("<p>", "").replace("</p>", "").replace("<br />", "").replace("&ldquo",'“').replace("&rdquo",'”').replace("&hellip",'...')
            self.writetofile(str,myfile)


myspider =spider()
myfile = open("./duanzi.txt", 'a')  # 追加内容
for i in range(0,400):
    l = myspider.loadpage(i)
    myspider.printonepage(i, l)
    #i+=1
myfile.close()
# l=myspider.loadpage(1)
# myspider.printonepage(1,l)
