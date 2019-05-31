import  xlrd
##最小二乘法
import numpy as np  ##科学计算库
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
np.seterr(divide='ignore', invalid='ignore')

plt.rcParams['axes.unicode_minus']=False
data = xlrd.open_workbook('sort2.xls') # 打开xls文件
table={}
for i in range(10):
    print(i)
    table[i]=data.sheets()[i]
alldata=[]##收集
preview2018=[]#预测2018
real2018=[]#2018实际
e=[]##估值
name=[]
for i in range(2719):
    if i == 0 or i == 1:  # 跳过第一行
        continue
    a=[]
    for j in range(9):
        a.append(table[9-j].row_values(i)[2])
    real2018.append(table[0].row_values(i)[2])##2018的数据
    alldata.append(a)
print(alldata[100])#公司的2009-2017数据
dta=np.array(alldata[3],dtype=np.float)
dta=pd.Series(dta)
dta.index=pd.Index(sm.tsa.datetools.dates_from_range('2009','2017'))
# dta.plot(figsize=(9,6))
# plt.show()
# fig=plt.figure(figsize=(9,6))
# ax1=fig.add_subplot(111)
# diff1=dta.diff(1)
# diff1.plot(ax=ax1)
# plt.show()

diff1=dta.diff(1)
fig=plt.figure(figsize=(9,6))
ax1=fig.add_subplot(211)
fig=sm.graphics.tsa.plot_acf(dta,lags=8,ax=ax1)
ax2=fig.add_subplot(212)
fig=sm.graphics.tsa.plot_pacf(dta,lags=8,ax=ax2)

plt.show()

arima = ARIMA(dta, order=(1, 1, 1))
result = arima.fit(disp=True)
print(result.aic, result.bic, result.hqic)
print(diff1)
plt.plot(diff1)
plt.plot(result.fittedvalues, color='red')
plt.title('ARIMA RSS: %.4f' % sum(result.fittedvalues ) ** 2)
plt.show()

# 模型预测
pred = result.predict('2017', '2018', dynamic=True)
print(pred)

fig,ax=plt.subplots(figsize=(9,6))
ax=dta.ix['2008':].plot(ax=ax)
print(ax)
fig=result.plot_predict('2017','2018',dynamic=True,ax=ax,plot_insample=False)
plt.show()
print('end')



