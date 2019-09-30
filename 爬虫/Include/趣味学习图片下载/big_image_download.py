import  requests
from  urllib import  parse
from bs4 import BeautifulSoup
import re
import json
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Cookie': 'wluuid=66;  ',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'connection': 'keep-alive'
    , 'Host': 'stock.tuchong.com',
    'Upgrade-Insecure-Requests': '1'
    }
def mkdir(path):
    import os# 引入模块
    path = path.strip()# 去除首位空格
    path = path.rstrip("\\") # 去除尾部 \ 符号
    isExists = os.path.exists(path)  # 判断路径是否存在  # 存在     True # 不存在   False
    if not isExists:  # 判断结果
        os.makedirs(path)# 如果不存在则创建目录 # 创建目录操作函数
        return True#print (path + ' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print(path + ' 目录已存在')
         return False
def downloadimage(imageid,imgname):
    url = 'https://weiliicimg9.pstatp.com/weili/l/'+str(imageid)+'.webp'
    url2 = 'https://icweiliimg9.pstatp.com/weili/l/'+str(imageid)+'.webp'
    b=False
    r = requests.get(url)
    print(r.status_code)
    if(r.status_code!=200):
        r=requests.get(url2)
    with open(imgname+'.jpg', 'wb') as f:
        f.write(r.content)
        print(imgname+" 下载成功")
def getText(text,free):
    texturl = parse.quote(text)
    url="https://stock.tuchong.com/"+free+"search?term="+texturl+"&use=0"
    req=requests.get(url,headers=header)
    soup=BeautifulSoup(req.text,'lxml')
    js=soup.select('script')
    js=js[4]
    print(js)
    pattern = re.compile(r'window.hits = (\[)(.*)(\])')
    va = pattern.search(str(js)).group(2)#解析js内容
    print(va)
    va = va.replace('{', '{').replace('}', '},,')
    print(va)
    va = va.split(',,,')
    print(va)
    index = 1
    for data in va:
        try:
             dict = json.loads(data)
             print(dict)
             imgname='img2/'+text+'/'+dict['title']+str(index)
             index+=1
             mkdir('img2/'+text)
             imgid=dict['imageId']
             downloadimage(imgid,imgname)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    num=input("高质量大图带水印输入1，普通不带水印输入2:")
    num=int(num)
    free=''
    if num==2:
        free='free'
    text = input('输入关键词:')
    getText(text,free)