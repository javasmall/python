import numpy as np
from scipy.optimize import leastsq#最小二乘法运算库
import  matplotlib.pyplot as plt
xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.87])
yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.26])
def func(p,x):
    k,b=p
    print('K:',k,'B:',b)
    return  k*x+b
def error(p,x,y):

    return  func(p,x)-y
p0=[100,2]

Para=leastsq(error,p0,args=(xi,yi))
print(Para)
k,b=Para[0]
print("k=",k,"b=",b)
plt.figure(figsize=(8,6))
plt.scatter(xi,yi,color='red',label='sample point',linewidths=2)
x=np.linspace(1,10,1000)#k,b已经确定，两点确定一个直线
y=k*x+b
plt.plot(x,y,color='orange',label='fitting line' ,linewidth=2)
plt.legend()
plt.show()