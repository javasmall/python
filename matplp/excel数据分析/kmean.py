from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['axes.unicode_minus']=False
data = xlrd.open_workbook('2019-51MCM-Problem C-Appendix 1.xls') # 打开xls文件
table=data.sheets()[0]
a=[]
b=[]
c=[]
for i in range(2,1508):

    if table.row_values(i)[4]=='' or table.row_values(i)[5] == '' or table.row_values(i)[6] == '':
       continue
    else:
        a.append((table.row_values(i)[4]))
        b.append((table.row_values(i)[5]))
        c.append((table.row_values(i)[6]))
print(a)#营业收入
print(b)#归母净利润
print(c)#净资产收益率
x=np.array(a)
y=np.array(b)
z=np.array(c)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(13, 9))  ##指定图像比例： 8：6

# plt.subplots_adjust(bottom=0.2)
#plt.plot(b, c, color="blue", label="数据关联性分析")
plt.scatter(a, c, color="red", label="数据分布")
plt.xlabel("营业收入")
plt.ylabel("归母净利润")
plt.xlim(-4000000000,9000000000)
plt.ylim(-50,50)
# plt.xticks(range(0,24),rotation=75,fontsize=10)#设置横坐标显示24次。
# plt.yticks(range(0,1000,50))

plt.legend()
plt.savefig('中国净资产收益率归母净利润关系')
plt.show()


