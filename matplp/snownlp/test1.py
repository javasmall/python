# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import  numpy as np
x=[1,2,3,4,5,6,7,8]
y=[6,8,4,2,8,6,4,7]
x=np.array(x)
y=np.array(y)
plt.plot(x,y,label='hello')
plt.legend()
plt.show()
# text = '''
# 喜欢
# '''
# text2='''
# 蠢货
# '''
# text3=text2+','+text
# s=SnowNLP(text)
# print(s.sentiments)