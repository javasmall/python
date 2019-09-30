import requests
from bs4 import BeautifulSoup

url='https://passport.csdn.net/v1/register/pc/login/doLogin'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
 'referer':'https://passport.csdn.net/login?code=public',
 'origin':'https://passport.csdn.net',
 'content-Type':'application/json;charset=UTF-8',
 'x-requested-with':'XMLHttpRequest',
 'accept':'application/json, text/plain, */*',
 'accept-encoding':'gzip, deflate, br',
 'accept-language':'zh-CN,zh;q=0.9',
 'connection': 'keep-alive'
 ,'Host': 'passport.csdn.net'
 }
s = requests.Session()#定义一个全局session
url1='https://blog.csdn.net/'
req=s.get(url1)

cookies=requests.utils.dict_from_cookiejar(s.cookies)
for va in cookies:
 print(va)
data='{"loginType":"1","pwdOrVerifyCode":"52cuihuini!",' \
 '"userIdentification":"1315426911@qq.com","uaToken":"119#Ml7hwm3IszUgUMMz1CEJyqUwcIxnSg2hD01oYJqqpqTd0PYiVDny2/2ECZLV7LJM/1gwL3UG7d238sNc2jTIa0hc6pp9QYkajrz2/RPW+kFDu4ihjFA4bwbUVSIOhB9bzYxr3Pd04yyo9gaeURSMo5zh/4LnDCEdsxesaB5/Rge3rj7el2I5dtZZC88o5akuA/G166YnPU4nhfuexAUi6X/jUgK3j8rmVzSyRRhh63/FM5A1qdAOclXjG18uoNsscz090orEKZ5bCjHsqEzOcXFjmRzneMvTC/U0AzhnI+momNf9gFgTBIMH0t9T81puDmSEdijpJW3TtQ+OyzOOX3uCcBw4eauYksgjNycnFAVCyHIvvC3JAgZzH04z6r0WG+Y+6VpmmPKdjyxAMbbJE4iKYbZD7zGL/GEMQEoGxtdrZ7oz7SX50DadDk67OBfkhbmLyBIiB4tSObLmEdf2kEdlEihNRnqVLfON+ln6lUd36PN1+8bAovCD5GsckZkh3UqIVMYk6aRhDOziywOnjb6ImSISQAW3a0fK0YZGgFH5Sc/Sxh3rxv9eY9CIko9WrI2Kqe1ZmVcjGqTt4dZyKTNRMV0I3wgF9U+S4lkG2rHj5mjVRt8GfCuICBlcxOILuUIMRuM23oALRJX6XXdYfUw96Pse3AAL9U+S4lkLo/I8R2VVXQgiFG5SfQ9D3/vL02+g46Oyl1A8QS0OjWM+uwE4PBsUdAHLfUB2BfxMa6ILRpInENHDHeAlRPSUdGXL9UNlKNuGdA9QRJBONNFL93vSRBse3AHhM2CW4XwsoUMU6qZ6qO14SCqOfoeJkl3QQ4IcaodRKAXpI7x7k2QXMewaup5fB+V6SZZH1gqpVFCSquKiqiTd8FoGBddDeT58+WgQietZaPOKnNEk7zUAEBd1Z5A/Au0LeRWxLMdHJ2PDmvU0EmL2vDYsmGQ0fCn3bE6RVz2BG+T3da/GX1eLJgMpJTJOVursg/rXWbHTrVi2m/o7PbdEcBLyXh+Dy0WtTFo/aaSNxgxll2Lq/c1ecPZ08okHHvfLEyGHHUfwGTRZ2qyDQLxu5CLk5l3wVOMbSqF9TZTMxvfZKnxdP+vZURCKaS/N8D0H+jUptHkUM0419J8REti8f8wEcUfANvu8LweWXHYJ3wyMbuRRLZUZ3BTgnwGW5uyEGS7gk11V5pRUxqKnvF/XdZWhJO2HYZEC34R9wCLonbVg2uuG8qmapBz5Vv4rIqzCdDr/LEmKbdFVHPz2M2Owbj/okqH8u3/SHmxeT3UhZX1WsgcnjlSQ3WkMxzDT4Md//Cmrtv5nY38+ZdyrnSLg/NLYCP4t65vXOdn2n3VAuhAfBwpSvNiVvBZGpHldW6PAFpHYZIqImbMQstBuDRrimFmr6L5Pv1FFjjS6RTBUDCB0v+Q6OU6GcGFgd93qLPyaWX3KfWTMemxGd8ATpACxOo97J7rBTC2ReIRVG8wmpzL5TO==",' \
 '"webUmidToken":"T07ACF4C0E6DD05E0C2D5C01A0FA3D7D6CAA1628EBE9618A4698ACA4D53"}'
req=s.post(url,data=data,headers=header)
cookies = requests.utils.dict_from_cookiejar(s.cookies)
res=req.text
print(res)
print(req.status_code)


# url2='https://blog.csdn.net/nav/watchers'
# req2=requests.get(url2,cookies=cookies)
# soup=BeautifulSoup(req2.text,'lxml')
#
# print(soup.text)
