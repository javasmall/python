from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.iloveyou.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req,timeout=4)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e)