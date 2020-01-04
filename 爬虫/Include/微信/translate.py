#更多请关注公众号：bigsai
import itchat
import requests
import hashlib
import time
import urllib.parse

jud=False#默认是先不开启
isreturn=False#是否回复
To='en'#翻译成的语言默认是英语

def nmd5(str):#md5加密
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return  str_md5
def formdata(transtr):
    # 待加密信息
    global To
    headerstr = '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    bv=nmd5(headerstr)
    ts=str(round(time.time()*1000))
    salt=ts+'90'
    strexample='fanyideskweb'+transtr+salt+'n%A-rKaT5fb[Gy?;N5@Tj'
    sign=nmd5(strexample)
    i=len(transtr)
    dict={'i':transtr,'from':'AUTO','to':To,'smartresult': 'dict',
          'client':'fanyideskweb',
          'salt':salt,
          'sign':sign,
          'ts':ts,
          'bv':bv,
          'doctype':'json',
          'version':'2.1',
          'keyfrom':'fanyi.web',
          'action':'FY_BY_REALTlME'
    }
    return dict
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
 'Referer':'http://fanyi.youdao.com/',
 'Origin': 'http://fanyi.youdao.com',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'X-Requested-With':'XMLHttpRequest',
 'Accept':'application/json, text/javascript, */*; q=0.01',
 'Accept-Encoding':'gzip, deflate',
 'Accept-Language':'zh-CN,zh;q=0.9',
 'Connection': 'keep-alive',
 'Host': 'fanyi.youdao.com',
 'cookie':'_ntes_nnid=937f1c788f1e087cf91d616319dc536a,1564395185984; OUTFOX_SEARCH_USER_ID_NCOO=; OUTFOX_SEARCH_USER_ID=-10218418@11.136.67.24; JSESSIONID=; ___rl__test__cookies=1'
 }
itchat.auto_login(hotReload=True)#登录


# 注册消息响应事件，消息类型为itchat.content.TEXT，文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 返回信息调用信息
    global jud
    global To
    global  isreturn
    text=msg['Text']
    dict = formdata(text)
    if "翻译模式" in text:
        isreturn =True
    elif "停止翻译" in text:
        isreturn=False
    if  "开始" in text:
        jud=True
    elif  "停止" in text:
        jud=False
    elif "英语" in text:
        To = 'en'
    elif "日语" in text:
        To = 'ja'
    elif "韩语" in text:
        To = 'ko'
    elif "法语" in text:
        To = 'fr'
    if jud:#说明需要运行
        dict['to']=To
        dict['from']= 'AUTO'
        dict = urllib.parse.urlencode(dict)
        dict = str(dict)
        req = requests.post(url, timeout=1, data=dict, headers=header)
        val = req.json()
        transtr = val['translateResult'][0][0]['tgt']
        print(msg)
        itchat.send(transtr, toUserName=msg['ToUserName'])
    ##返回监听对面说的话
    if isreturn:
        dict['from']='AUTO'
        dict['to']='zh-CHS'##翻译成中文
        dict = urllib.parse.urlencode(dict)
        # dict = str(dict)
        req = requests.post(url, timeout=1, data=dict, headers=header)
        val = req.json()
        transtr = val['translateResult'][0][0]['tgt']
        print(msg)
        return 'ta说：'+str(transtr)#这个加上是如果对面发消息的监听。比如你是双向翻译可以尝试下
# 绑定消息响应事件后，让itchat运行起来，监听消息
itchat.run()