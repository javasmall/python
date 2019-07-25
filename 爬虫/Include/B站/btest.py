import requests
from bs4 import  BeautifulSoup
import json
import urllib.parse
## 只需要更改page
url="https://s.search.bilibili.com/cate/search?callback=jqueryCallback_bili_&main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=17&pagesize=20&jsonp=jsonp&time_from=20190716&time_to=20190723&_=1"
data={'page':1}
for page in range(1,10):
    data['page']=page
    req=requests.get(url,data=data)
    res=req.text
    res=res.replace("jqueryCallback_bili_","")
    res=res[1:(len(res)-1)]
    res=json.loads(res)
    result=res['result']
    for val in result:
        print(val['author'],'播放：',val['play'],'喜欢',val['favorites'],'review',val['review'])
