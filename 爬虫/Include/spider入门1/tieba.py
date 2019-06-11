
# -*- coding:utf-8 -*-
from urllib import request as urllib2
from urllib import parse
import random

def loadPage(url, page):
    '''
    根据url获取服务器响应文件
    url:需要爬取的url
    '''
    print('---------正在下载页面%d-------' % page)
    ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    ]
    header = random.choice(ua_list)
    request = urllib2.Request(url)
    request.add_header('User-Agent', header)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def write(html, page):
    '''
    将html文件写入本地
    :param html: 服务器响应文件内容
    :return:
    '''
    data = html
    file_name = 'tieba{}.txt'.format(page)
    print('---------正在保存文件%s-------'%file_name)
    # 运用with open as语句使代码更加简洁 避免写异常处理和文件关闭语句
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(data.decode())
    print('---------success!---------')


def tiebaSpider(url, kw, begin, end):
    '''
    爬取贴吧信息
    '''
    words = {
        'kw':kw
    }
    kw = parse.urlencode(words)
    url = url % (kw)
    for page in range(begin, end + 1):
        pn = ((page-1)*50)
        ful_url = url + str(pn)
        html = loadPage(url, page)
        write(html, page)

if __name__ == '__main__':
    kw = input('请输入爬取贴吧名:')
    beginPage = int(input('请输入起始页:'))
    endPage = int(input('请输入结束页:'))
    url = r'http://tieba.baidu.com/f?%s&pn='
    tiebaSpider(url, kw, beginPage, endPage)