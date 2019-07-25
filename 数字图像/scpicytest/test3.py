##最小二乘法
import numpy as np  ##科学计算库
import scipy as sp  ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
from scipy.optimize import leastsq  ##引入最小二乘法算法
from bs4 import BeautifulSoup
import requests

#获取数据
#print("请输入学号")
id='10000000412'
url="http://www.overlove.xin/ssm/pastrank?id="+id#+"&type=classrank"
req=requests.get(url)
dates=req.json()
score=[]
rank=[]
index=[]
i=0
for date in dates:
    score.append(int(date['sumscore']))
    rank.append(int(date['rank1']))
    index.append(i)
    i+=1
#样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Yi = np.array([5.25, 2.83, 6.41, 6.71, 5.1, 4.23, 5.05, 1.98, 10.5])
Xi=np.array(index)
Yi=np.array(rank)


##需要拟合的函数func :指定函数的形状
def func(p, x):
    k, b = p
    return k * x + b
##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p, x, y):
    return func(p, x) - y
# k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0 = [100, 2]

# 把error函数中除了p0以外的参数打包到args中(使用要求)
Para = leastsq(error, p0, args=(Xi, Yi))

# 读取结果
k, b = Para[0]
# print("k=", k, "b=", b)
# print("cost：" + str(Para[1]))
# print("求解的拟合直线为:")
# print("y=" + str(round(k, 2)) + "x+" + str(round(b, 2)))

# 画样本点
plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
plt.scatter(Xi, Yi,color="red", label='sample point', linewidths=3)
#添加新的点
len=len(index)
Xnew=len
Ynew=Xnew*k+b
plt.scatter(Xnew,Ynew,color='green',label='forecast point',linewidths=3)
# 画拟合直线
x = np.linspace(0, 8, 1000)  ##在0-15直接画100个连续点
y = k * x + b  ##函数式
plt.plot(x,y, color='orange', label='fitting line', linewidth=1)
plt.ylim(0,500)
plt.legend()  # 绘制图例
plt.show()