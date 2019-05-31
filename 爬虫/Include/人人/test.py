import json
from urllib import request, parse

# 保存cookie
from http import cookiejar

# 通过对象保存cookie
cookie_object = cookiejar.CookieJar()
# handler 对应着一个操作
handler = request.HTTPCookieProcessor(cookie_object)
# opener 遇到有cookie的response的时候,
# 调用handler内部的一个函数, 存储到cookie object
opener = request.build_opener(handler)

# url
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018722024835'
# form
form = {
    'email': '',  # 用户名
    'password': '455148ff24ecadda4e241f2797b5ab51ce9725c7df8cf0204638c0e60b1e557c',  # 这是加密后的密码
    'rkey': 'f2758794667a236f9fe7db56c6b10a7d',

}
# post
form_bytes = parse.urlencode(form).encode('utf-8')

response = opener.open(url, form_bytes)

html_bytes = response.read()
# html_bytes = post(url, form=form)
# 打印结果
# print(html_bytes)
# 通过json获取一个字典类型
res_dict = json.loads(html_bytes.decode('utf-8'))

home_url = res_dict['homeUrl']

# 访问页面
response = opener.open(home_url)
html_bytes = response.read()
print(html_bytes.decode('utf-8'))

# 根据自己登陆的信息，修改 url和form中的email项 password，rkey，f这几项就可不用登录账号直接进入网页爬取信息，登录后刷新网页找到login里的headers信息

