import  requests
from  bs4 import BeautifulSoup
header={

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control':'max-age=0',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        #'if-modified-since':'Mon, 05 Nov 2018 03:38:51 GMT',
        #'Host':'passport.csdn.net',

        'Upgrade-Insecure-Requests':'1',
        'Cookie':'anonymid=jo41mgbm-fs2rfu; depovince=ZGQT; _r01_=1; __utma=151146938.1112932348.1541377755.1541377755.1541377755.1; __utmz=151146938.1541377755.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ln_uact=18796011370; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20120804/1510/h_main_PFAa_58ec00000d9d1376.jpg; l4pager=0; jebecookies=0e37fa8f-7ae6-4d3c-91eb-530dbc01111d|||||; JSESSIONID=abc3fdyUUkPwZgbxpSNBw; ick_login=4ae55c8d-dffe-4bfe-8ea2-470257ee8872; jebe_key=1fac2c6b-8a91-4124-b739-87d990a60046%7Cbcb64fc80ef2a62b07325c0d1e76de56%7C1541406637662%7C1%7C1541485429877; _de=F1AF69EBB6C45DEEC69E456A645C257F; p=923db06e1fef271d1913ae7538df141e8; first_login_flag=1; t=fc5a31391cf5a6110644aa0c00143fa18; societyguester=fc5a31391cf5a6110644aa0c00143fa18; id=347944598; xnsid=184eef71; ver=7.0; loginfrom=null; wp_fold=0'
}
cookies={ 'Cookie': 'smidV2=20181027082831a234f8b1e1251c39c06a282ff811ad98007243868e4a6ce10; ARK_ID=JS61aa45f32c8614772aea7378bdb439b561aa; UN=qq_40693171; uuid_tt_dd=10_28867322980-1540783272858-653076; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; UM_distinctid=166ca1eb93e18a-0e69267fa656e9-36664c08-144000-166ca1eb93f2ad; dc_session_id=10_1541462161768.631834; UserName=qq_40693171; UserInfo=UL%2BdYdZEDjAxoM0a%2BWlyer3AuOCS%2Fpe3eS9TnaJsY%2FjIpA8i9xJ8OSljPIFrYpmVwIJkapj%2Fl3Mg1nUZEq7Z8s78%2B5MvvIqzI37%2FosurXRJJSC7TAjab7ktsLyUI%2F2b9J6sBF0Kt0poSV4j95ilzoQ%3D%3D; UserNick=%E5%A5%BD%E6%B1%82%E7%AA%88%E7%AA%95; AU=CE8; BT=1541464775670; UserToken=UL%2BdYdZEDjAxoM0a%2BWlyer3AuOCS%2Fpe3eS9TnaJsY%2FjIpA8i9xJ8OSljPIFrYpmVwIJkapj%2Fl3Mg1nUZEq7Z8s78%2B5MvvIqzI37%2FosurXRJJSC7TAjab7ktsLyUI%2F2b9LjKOjZOi1zlFGv0XHlBT5T98cwS9RJhtdyIoM%2FEP69%2Bsr8I9YUyftrxmtH1oab70; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1541433364,1541435133,1541435367,1541436290; dc_tos=phqcej; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1541437004'}
dir={}
url='http://www.renren.com/347944598'
url2='https://passport.csdn.net/account/verify'
# sess=requests.Session()
# req=sess.get(url,headers=header)
# html=req.text
# soup=BeautifulSoup(html,'lxml')
# form=soup.select('#fm1')[0]
# team=form.find_all('input')
# for q in team:
#     name=q.get('name')
#     value=q.get('value')
#     if name=='username':
#         value='1315426911@qq.com'
#     if name=='password':
#         value='52cuihuini'
#     if name!=None:
#        print(name,value)
#        dir[name]=value
# print(dir)
# dir['fkid']='WC39ZUyXRgdHuPbwcuUATFAtJiPDdAvr2Wl7YlOivS/4rODMUok/r/GOdbhLKdNPjpkVwP6cNW+HzWwC1T+qYgBiF9UCWDdo3E6zicfHluGEEFGfBgBBSmnmOFg7mZIOpkJlhk/gbBtr8WQCkkJTqhEZ8pCNkGi2yQhzpvB+jhXiTq8yj0ZUKk1e8lIFHzgXZAD9XWhrlL373mL1ammYffmXVx3MLNXO/T+1oLB3HVw51cvionFIHc3ZLz3B3BTr3oliTdwC2z74%3D1487577677129'
# dir['UN']='qq_40693171'
# dir['JSESSIONID']='FDBFA23971F485202F27A4C22739812A.tomcat2'
# dir['smidv2']='20181027082831a234f8b1e1251c39c06a282ff811ad98007243868e4a6ce10'
value=requests.get(url,headers=header)
html=value.text
soup=BeautifulSoup(html,'lxml')
link=soup.text
print(soup)

