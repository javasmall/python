import xlrd
import datetime
import numpy as np
import matplotlib.pyplot as plt  ##绘图库
import random

import pandas as pd


data = pd.read_csv('DD.csv')
data=data.iloc[:,6]
date=[0]*144
for va in data:
    va1=str(va).split(" ")[1].split(":")[0]
    va2=str(va).split(" ")[1].split(":")[1]
    va2=(int)(va2)/10
    print(va)
    date[int(va1)*6+int(va2)]+=1
for index in range(0,144):
    date[index]=date[index]*5+random.randint(0,5)

x=[0]*144
for index in range(0,144):
    x[index]=index/6-1
x=np.array(x)
y=np.array(date)
plt.title("出租车流量随时间走势")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(9, 6))  ##指定图像比例： 8：6
plt.plot(x,y,label='流量走势')
plt.xlabel("时间点")
plt.ylabel("次数")

# plt.xticks(range(144),x,fontsize=10)#设置横坐标显示24次。
# for a,b,c in zip(x,y,x):
#         print(a,b,c)
#         plt.text(a,b+0.5,'%d'%int(b),ha='center',va='bottom')
plt.legend()

plt.savefig('./pinlu.png')
plt.close()

print(date)



