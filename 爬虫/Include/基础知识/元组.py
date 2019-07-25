a1=(88,99,'张赛')
for a in a1:
    print('%s '%a,end='')
print('\n')
print(a1[2]+'eheh')
#index count

info={'name':'zhangsai','age':100}
print(info['name'])
age=info.get('name')
print(age)#没有的化会报noll

info = {'name': '班长', 'sex': 'f', 'address': '地球亚洲中国北京'}

print('删除前,%s' % info['name'])
#删除操作
del info['name']

print('删除后,%s' % info['sex'])

info = {'name': 'monitor', 'sex': 'f', 'address': 'China'}

print('清空前,%s' % info)

info.clear()

print('清空后,%s' % info)
info=['','']