import urllib.request
import json
# 提取json格式信息的库
import jsonpath
# 存取进xls文件的库
import xlwt

n = 0
myxls = xlwt.Workbook()
sheet1 = myxls.add_sheet(u'yx', cell_overwrite_ok=True)
# write(i,j,value)存取文档的首行
sheet1.write(0, 1, "公司名")
sheet1.write(0, 2, "地区")
sheet1.write(0, 3, "公司人数")
sheet1.write(0, 4, "类型")
sheet1.write(0, 5, "公司网站")
sheet1.write(0, 6, "岗位需求")
sheet1.write(0, 7, "要求毕业性质")
sheet1.write(0, 8, "薪资")
sheet1.write(0, 9, "工作性质")
sheet1.write(0, 10, "福利")

for i in range(1, 10):
    url3 = "https://fe-api.zhaopin.com/c/i/sou?start=" + str(
        i * 90) + "&pageSize=90&cityId=530&industry=160400&workExperience=-1&education=4&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.20600649&x-zp-page-request-id=a0a5c8da8e5e455ca30312a4d85fa52d-1548559285341-380683"
    req = urllib.request.Request(url3)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE")
    data = urllib.request.urlopen(req).read()
    data = json.loads(data)
    jobName = jsonpath.jsonpath(data, '$..jobName')
    searchTag = jsonpath.jsonpath(data, "$..searchTag")

    company = jsonpath.jsonpath(data, "$..company")
    companyName = jsonpath.jsonpath(data, "$..company.name")
    companyPeopleNum = jsonpath.jsonpath(data, "$..company.size.name")
    companyType = jsonpath.jsonpath(data, "$..company.type.name")
    companyUrl = jsonpath.jsonpath(data, "$..company.url")

    city = jsonpath.jsonpath(data, "$..city")
    cityName = jsonpath.jsonpath(data, "$..city.display")

    workingExp = jsonpath.jsonpath(data, "$..workingExp")
    workingExpName = jsonpath.jsonpath(data, "$..workingExp.name")

    jobType = jsonpath.jsonpath(data, "$..jobType")
    jobTypeName = jsonpath.jsonpath(data, "$..jobType.display")

    eduLevel = jsonpath.jsonpath(data, "$..eduLevel")
    eduLevelName = jsonpath.jsonpath(data, "$..eduLevel.name")

    welfare = jsonpath.jsonpath(data, "$..welfare")
    salary = jsonpath.jsonpath(data, "$..salary")
    emplType = jsonpath.jsonpath(data, "$..emplType")
    jobTag = jsonpath.jsonpath(data, "$..jobTag.searchTag")

    for i in range(0, 89):
        print("公司编号：" + str(n))
        print(companyName[i])
        print(cityName[i])
        print(companyPeopleNum[i])
        print(companyType[i])
        print(companyUrl[i])
        print(workingExpName[i])
#        print(jobTypeName[i])
        print(eduLevelName[i])
        # print(welfare[i])
        print(salary[i])
        print(emplType[i])
#        print(jobTag[i])
        print()
        n = n + 1
        sheet1.write(n, 0, n)
        sheet1.write(n, 1, companyName[i])
        sheet1.write(n, 2, cityName[i])
        sheet1.write(n, 3, companyPeopleNum[i])
        sheet1.write(n, 4, companyType[i])
        sheet1.write(n, 5, companyUrl[i])
#        sheet1.write(n, 6, jobTypeName[i])
        sheet1.write(n, 7, eduLevelName[i])
        # sheet1.write(n,8,welfare[i])
        sheet1.write(n, 8, salary[i])
        sheet1.write(n, 9, emplType[i])
#        sheet1.write(n, 10, jobTag[i])

myxls.save('yx.xls')