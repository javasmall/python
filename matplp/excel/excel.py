import  xlrd
##最小二乘法
import numpy as np  ##科学计算库
import scipy as sp  ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
plt.rcParams['axes.unicode_minus']=False
from scipy.optimize import leastsq  ##引入最小二乘法算法
data = xlrd.open_workbook('sort2.xls') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
table1 = data.sheets()[1] # 打开第一张表
table2 = data.sheets()[2] # 打开第一张表
table3 = data.sheets()[3] # 打开第一张表table = data.sheets()[0] # 打开第一张表
table4 = data.sheets()[4] # 打开第一张表
table5 = data.sheets()[5] # 打开第一张表
table6 = data.sheets()[6] # 打开第一张表
table7 = data.sheets()[7] # 打开第一张表
table8 = data.sheets()[8] # 打开第一张表
table9 = data.sheets()[9] # 打开第一张表
nrows = table.nrows      # 获取表的行数
sum=0.0

##需要拟合的函数func :指定函数的形状
def func(p, x):
    k, b = p
    return k * x + b
##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p, x, y):
    return func(p, x) - y
# k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0 = [100, 2]



b=[]##收集
c=[]#预测2018
d=[]#2018实际
e=[]##估值
name=[]
for i in range(2719):
    if i == 0 or i == 1:  # 跳过第一行
        continue
    a=[]
    a.append(table9.row_values(i)[2])
    a.append(table8.row_values(i)[2])
    a.append(table7.row_values(i)[2])
    a.append(table6.row_values(i)[2])
    a.append(table5.row_values(i)[2])
    a.append(table4.row_values(i)[2])
    a.append(table3.row_values(i)[2])
    a.append(table2.row_values(i)[2])
    a.append(table1.row_values(i)[2])
    d.append(table.row_values(i)[2])##2018的数据
    name.append(table.row_values(i)[2])
    b.append(a)

    #print(a)
#print(b)
x=[1,2,3,4,5,6,7,8,9]
#print(b[7])
for arrary in b:
    lenth=9
    # print(arrary)
    list=[]
    for j in range(1,7):
        if abs(arrary[j]-arrary[j-1])>5.0 :
            if arrary[j-1]>0:
                if abs(arrary[j]/arrary[j-1])>5.0:
                   list.append(arrary[j])
    lenth=lenth-list.__len__()
    #print(lenth)
    for k in list:
        arrary.remove(k)
    xi=np.arange(int(lenth))
    yi=np.array(arrary)
    # 把error函数中除了p0以外的参数打包到args中(使用要求)
    Para = leastsq(error, p0, args=(xi, yi))

    # 读取结果
    k, b = Para[0]
    # plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
    # plt.scatter(xi, yi, color="red", label='sample point', linewidths=3)
    #添加新的点
    len = 9
    Xnew = len+1
    Ynew = Xnew * k + b
    c.append(Ynew)
    # plt.scatter(Xnew, Ynew, color='green', label='forecast point', linewidths=3)
    # # 画拟合直线
    # x = np.linspace(0, 10, 1000)  ##在0-15直接画100个连续点
    # y = k * x + b  ##函数式
    # plt.plot(x, y, color='orange', label='fitting line', linewidth=1)
    # plt.ylim(0, 10)
    # plt.legend()  # 绘制图例
    # plt.show()
sum=0.0
sum2=0.0
sum3=0.0
for i in range(2717):
    #print(c[i],d[i])
    te=c[i]-d[i]
    sum2=sum2+c[i]
    sum3=sum3+d[i]
    sum=sum+abs(c[i]-d[i])
    if d[i]==0:
        e.append(0)
    else:
        e.append(te/d[i])
# print(e)
# print(name)
x3=np.arange(2717)
y3=np.array(e)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(12, 9))  ##指定图像比例： 8：6
plt.plot(x3,y3,label='估值溢价',linewidth=-1)
print(sum,sum2)
plt.ylim((-40,50))
plt.xlabel("公司")
plt.ylabel("溢价")
plt.legend()
plt.show()
print(c)
print(d)
sum=sum/2717##标准差
sum2=sum2/2717#预测值
sum3=sum3/2717#实际值
va=(sum2-sum3)/sum3
print(sum,sum2,sum3,va)













