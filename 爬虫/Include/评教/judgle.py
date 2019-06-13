#江科大一键评教
import requests
from bs4 import BeautifulSoup
import re
def judteacher(url,cookiedict):
    res=requests.get(url,cookies=cookiedict)
    html=res.text
    soup=BeautifulSoup(html,'lxml')
    form=soup.select('form')[0]
    actionurl='http://jwgl.just.edu.cn:8080'+form.get('action')#需要post提交的表单

    allinput=form.select('input')
    dictkey={}
    for link in allinput:
        if  not str(link.get('type')).__eq__('button'):
            dictkey[str(link.get('name'))]=str(link.get('value'))
    buttoninput=form.select('#table1 tr')
    index=0
    for button in buttoninput:
       # print(index,button)
        if index==0:
            index+=1
            continue
        elif index==(buttoninput.__len__()-1):
            text=button.find('textarea').get('name')
            dictkey[text]='老师很负责任，收益良多'
        elif index==1:
            buttonselected=button.select('input[type=radio]')[1]
            dictkey[str(buttonselected.get('name'))]=str(buttonselected.get('value'))
        else:
            buttonselected = button.select('input[type=radio]')[0]
            dictkey[str(buttonselected.get('name'))] = str(buttonselected.get('value'))
        index+=1#第0个是没用的，第一个是选满意，剩下非常满意，倒数第一个是文本评论
    dictkey['tj'] = '提 交'
    dictkey['pj06xh'] = ["1","2","3","4","5"]
    dictkey['issubmit']="1"
    post=requests.post(actionurl,data=dictkey,cookies=cookiedict)
    print(dictkey)

def jud(url,cookiedict):
    res=requests.get(url,cookies=cookiedict)
    soup=BeautifulSoup(res.text,'lxml')
    teachers=soup.select('td a[href]')
    pattern=re.compile(r'.*[\'](.*)[\'].*')#正则提取javascrit：href='----'
    for teacherurl in teachers:
        teacherurl=str(teacherurl.get('href'))
        m=pattern.search(teacherurl)
        teacherurl='http://jwgl.just.edu.cn:8080'+str(m.group(1))#得到完整的teacherurl
        try:
           judteacher(teacherurl,cookiedict)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    url="http://jwgl.just.edu.cn:8080/jsxsd/"
    res=requests.get(url)
    cookiejar=res.cookies
    cookiedict=requests.utils.dict_from_cookiejar(cookiejar)

    html=res.text
    soup=BeautifulSoup(html,'lxml')
    data={}
    inputkey=soup.select("input")
    for canshu in inputkey:
        if not str(canshu.get("name")).__eq__(None):
            data[str(canshu.get('name'))]=canshu.get('value')
    data['USERNAME']='162210702236'
    data['PASSWORD']='zhongad3344'
    #  print(data)
    urlLogin=url+'xk/LoginToXk'
    res2=requests.post(urlLogin,data=data,cookies=cookiedict)


    url3=url+'xspj/xspj_find.do?Ves632DSdyV=NEW_XSD_JXPJ'
    res3=requests.get(url3,cookies=cookiedict)
    soup3=BeautifulSoup(res3.text,'lxml')
    hrefs=soup3.select("td a[href]")
    shiyan='http://jwgl.just.edu.cn:8080'+str(hrefs[0].get('href'))
    lilun='http://jwgl.just.edu.cn:8080'+str(hrefs[2].get('href'))
    jud(lilun,cookiedict)
    jud(shiyan,cookiedict)

