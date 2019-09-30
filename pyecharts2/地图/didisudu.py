import  csv
import numpy as np
import matplotlib.pyplot as plt  ##绘图库
csv_file=csv.reader(open('滴滴数据计算.csv','r'))
data=[]

for va in csv_file:
    try:

        if len(va[4])==1:
            va[4]='0'+va[4]
        data.append(va)
    except Exception as e:
        print(e)

data=np.array(data)
data = data[data[:,4].argsort()]
distancce=[]
minite=[]
speed=[]
hour=[]
for va in data:
 try:
    a1=float(va[1])
    a1=int(a1)
    print(a1,va[4])
    distancce.append((int)((float)(va[1])))
    minite.append((int)((float)(va[2])))
    speed.append((int)((float)(va[3])))
    hour.append(((float)(va[4])))
 except Exception as e:
     print(e)
x=np.array(minite)
y=np.array(speed)
X=np.arange(len(x))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(9, 6))  ##指定图像比例： 8：6
plt.title("出租车速度随时间走势")
plt.scatter(hour,speed,label='速度')
plt.xlabel("时间:hour")
plt.ylabel("速度:km/h")
plt.show()
