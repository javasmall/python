import xlrd
import numpy as np  ##科学计算库
import scipy as sp  ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
data = xlrd.open_workbook('2019-51MCM-Problem C-Appendix 1.xls') # 打开xls文件
table = data.sheets()[0] # 打开第一张表 2018
a=[]
def getvalue(tableindex):
    global a,table
    a=[]
    table=data.sheets()[tableindex]
    for i in range(2,1508):
        #print(table.row_values(i)[3])
        if not table.row_values(i)[3] :
            a.append(0)
        else:
            a.append(table.row_values(i)[3])
    for j in a:
        print(j)
getvalue(0)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

x3=np.arange(len(a))
y3=np.array(a)
plt.figure(figsize=(15, 10))  ##指定图像比例： 8：6
#plt.plot(x3,y3,label='2018市销率',linewidth = 0.5)

plt.xlabel("公司")
plt.ylabel("市销率")
getvalue(0)
x3=np.arange(len(a))
y3=np.array(a)
plt.scatter(x3, y3,color="red", label='2018中国公司市销率分布', linewidth=-1,alpha=0.8)
getvalue(1)
x3=np.arange(len(a))
y3=np.array(a)
plt.ylim(0,500)
#plt.scatter(x3, y3,color="green", label='2017', linewidth=-1,alpha=0.5)
plt.legend()
plt.savefig('中国2018市销率.jpg')
fenbu={'0,5':0,'5,50':0,'50,200':0,'200+':0}
for i in a:
    if i<3:
        fenbu['0,5']=fenbu['0,5']+1
    elif i<10:
        fenbu['5,50']=fenbu['5,50']+1
    elif i<50:
        fenbu['50,200']=fenbu['50,200']+1
    else:
        fenbu['200+']=fenbu['200+']+1
print(fenbu)
plt.show()