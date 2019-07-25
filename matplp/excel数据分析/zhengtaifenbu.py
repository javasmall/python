import xlrd
import numpy as np  ##科学计算库
import scipy as sp  ##在numpy基础上实现的部分算法库

import matplotlib.pyplot as plt  ##绘图库
plt.rcParams['axes.unicode_minus']=False
data = xlrd.open_workbook('sort2.xls') # 打开xls文件
table = data.sheets()[0] # 打开第一张表 2018

a=[]
b=[]
d=[]#差
e=[]#倍数
dd=[]
ee=[]
def getvalue(tableindex):
    global a,table
    a=[]
    table=data.sheets()[tableindex]
    for i in range(2,2719):
        #print(table.row_values(i)[3])
        if not table.row_values(i)[2] :
            a.append(0)
        else:
            a.append(table.row_values(i)[2])
    # for j in a:
    #     print(j)
getvalue(0)
b.extend(a)#2018
getvalue(1)

print(a)##2017
print(b)##2018
print(len(a),len(b))
print(d)
d=a
e=b
def jisuan():
    global d,e
    for i in range(2716):
        #print(b[i],a[i])
        d[i] = (b[i]-a[i])
        if a[i]==0:
            e[i]=0
        else:
            e[i]=(b[i]/a[i])
# jisuan()
# dd.extend(d)
# ee.extend(e)
for i in range(2,10):
    b=a
    getvalue(i)
    jisuan()
    dd.extend(d)
    ee.extend(e)

print(len(ee))
x3=np.arange(len(dd))
y3=np.array(dd)

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.plot(x3, y3,  color='red', label='fenbu', alpha=0.8)
# plt.ylim(-8000,8000)
# plt.xlim(0,22000)
# plt.xlabel("公司")
# plt.ylabel("数据差")
# plt.show()
# 倍数取500
# 增江取
def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
bei=['-∞,-1','-1,0','0,1','1,2','2,3','3,4','4,5','5,6','6,+∞']
beishu={bei[0]:0,bei[1]:0,bei[2]:0,bei[3]:0,bei[4]:0,bei[5]:0,bei[6]:0,bei[7]:0,bei[8]:0}
cha=['-∞,-20','-20,-5','-5,-2','-2,-1','-1,0','0,1','1,2','2,5','5,20','20,+∞']
chaju={cha[0]:0,cha[1]:0,cha[2]:0,cha[3]:0,cha[4]:0,cha[5]:0,cha[6]:0,cha[7]:0,cha[8]:0,cha[9]:0}
for i in dd:#差
    i=float(i)
    if i<-20:
        chaju[cha[0]]=chaju[cha[0]]+1
    elif i<-5:
        chaju[cha[1]] = chaju[cha[1]] + 1
    elif i<-2:
        chaju[cha[2]] = chaju[cha[2]] + 1
    elif i<-1:
        chaju[cha[3]] = chaju[cha[3]] + 1
    elif i<0:
        chaju[cha[4]] = chaju[cha[4]] + 1
    elif i<1:
        chaju[cha[5]] = chaju[cha[5]] + 1
    elif i<2:
        chaju[cha[6]] = chaju[cha[6]] + 1
    elif i < 5:
        chaju[cha[7]] = chaju[cha[7]] + 1
    elif i < 20:
        chaju[cha[8]] = chaju[cha[8]] + 1
    else:
        chaju[cha[9]] = chaju[cha[9]] + 1
for i in ee:#倍数
    i=float(i)
    if i<-1:
        beishu[bei[0]]=int(beishu[bei[0]])+1
    elif i>=-1 and i<0:
        beishu[bei[1]] = beishu[bei[1]] + 1
    elif i>=0 and i<1:
        beishu[bei[2]] = beishu[bei[2]] + 1
    elif i>=1 and i<2:
        beishu[bei[3]] = beishu[bei[3]] + 1
    elif i>=2 and i<3:
        beishu[bei[4]] = beishu[bei[4]] + 1
    elif i>=3 and i<=4:
        beishu[bei[5]] = beishu[bei[5]] + 1
    elif i>=4 and i<=5:
        beishu[bei[6]]= beishu[bei[6]]+1
    elif i>5 and i<=6:
        beishu[bei[7]]=beishu[bei[7]]+1
    else:
        beishu[bei[8]] = beishu[bei[8]] + 1
print(beishu)
xi=[]
yi=[]
for key in beishu:
    print(key)
    xi.append(key)
    yi.append(beishu[key])
plt.figure(figsize=(9, 7))  ##指定图像比例： 8：6
plt.bar(xi, yi, label='市销率倍数',color='red')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.plot(x3, y3,  color='red', label='fenbu', alpha=0.8)
# plt.ylim(-200,200)
# plt.xlim(0,22000)
plt.xlabel("相邻两年市场率倍数比分布")
plt.ylabel("总次数")
plt.savefig("相邻两年市场率倍数分布比")
plt.show()
plt.figure(figsize=(9, 7))  ##指定图像比例： 8：6
xj=[]
yj=[]
for key in chaju:
    xj.append(key)
    yj.append(chaju[key])
plt.bar(xj, yj, label='市销率差')


# plt.plot(x3, y3,  color='red', label='fenbu', alpha=0.8)
# plt.ylim(-200,200)
# plt.xlim(0,22000)
plt.xlabel("相邻两年市场率差数")
plt.ylabel("总次数")
#plt.savefig("美国相邻两年市场率倍数.png")
plt.show()
print(chaju)