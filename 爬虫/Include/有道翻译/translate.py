import requests
import hashlib
import time
import urllib.parse
# 创建md5对象
def nmd5(str):
    m = hashlib.md5()
    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return  str_md5
def formdata(transtr):
    # 待加密信息
    headerstr = '5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    #print(round(time.time()*1000))
    bv=nmd5(headerstr)
    ts=str(round(time.time()*1000))
    salt=ts+'90'
    strexample='fanyideskweb'+transtr+salt+'n%A-rKaT5fb[Gy?;N5@Tj'
    sign=nmd5(strexample)
    #print(sign)
    i=len(transtr)
    #print(i)
    # print('MD5加密前为 ：' + headerstr)
    # print('MD5加密后为 ：' + bv)
    dict={'i':transtr,'from':'AUTO','TO':'AUTO','smartresult': 'dict',
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
input=input("请输入翻译内容:")
dict=formdata(input)
dict=urllib.parse.urlencode(dict)
dict=str(dict)
#dict=urllib.parse.urlencode(dict).encode('utf-8')

req=requests.post(url,data=dict,headers=header)
val=req.json()
print(val['translateResult'][0][0]['tgt'])
