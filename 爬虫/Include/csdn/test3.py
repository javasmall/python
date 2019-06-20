import urllib.request,urllib.parse
import json,re

url = "https://fe-api.zhaopin.com/c/i/sou?"
kw_work = input("请输入您想查找的工作的关键字：")
city = input("请输入您想选择的城市：")
start_page = int(input("请输入开始爬取的页："))
end_page = int(input("请输入结束爬取的页："))
for page in range(start_page,end_page+1):
    data = {
        'start': page,
        'pageSize': '60',
        'cityId': city,
        'salary': '0,0',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'jobWelfareTag': '-1',
        'kw': kw_work,  # 输入搜索的关键字
        'kt': '3',
        '': '0',
        '_v': '0.08095475',
        'x-zp-page-request-id': 'a5a5b670d31c43b79fad5a8d98622136-1556194064568-484956'
    }
    url_now = url + urllib.parse.urlencode(data)  # 得到信息真实地址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    request = urllib.request.Request(url=url_now, headers=headers)
    response = urllib.request.urlopen(request)  # 发送请求，获取响应
    real_data = json.loads(response.read().decode())  # 此时real_data的类型为dict型
    print(real_data)
    # for data in real_data['data']['results']:
    #     data_list = []
    #     job_name = data['jobName']  # 工作名称
    #     data_list.append(job_name)
    #     job_salary = data['salary']  # 工作薪水
    #     data_list.append(job_salary)
    #     job_welfare = json.loads(data['positionLabel'])['jobLight']  # 此处与上面不同，必须先将其转化成字典之后再取值
    #     data_list.append(job_welfare)
    #     job_experence = data['workingExp']['name']  # 工作经验
    #     data_list.append(job_experence)
    #     job_eduLevel = data['eduLevel']['name']  # 学业水平
    #     data_list.append(job_eduLevel)
    #     job_company = data['company']['name']  # 公司名
    #     data_list.append(job_company)
    #     job_companytype = data['company']['type']['name']  # 公司性质
    #     data_list.append(job_companytype)
    #     job_url = data['positionURL']  # 详细的网站
    #     data_list.append(job_url)
    #     # 创建一个txt文件，将数据写入，或者也可以创建一个Excel表格将其写入，这里就不再举例
    #     with open('data.txt', 'a')as f:
    #         f.write(str(data_list))
    #         f.write("\n")
    #     f.close()
print("爬取成功！")
