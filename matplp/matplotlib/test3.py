import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#数据
name=['1','2','3','4']
colleges=[91,34,200,100]

#图像绘制
fig,ax=plt.subplots()
b=ax.barh(range(len(name)),colleges,color='#6699CC')

#添加数据标签
for rect in b:
    w=rect.get_width()
    ax.text(w,rect.get_y()+rect.get_height()/2,'%d'%int(w),ha='left',va='center')

#设置Y轴刻度线标签
ax.set_yticks(range(len(name)))
#font=FontProperties(fname=r'/Library/Fonts/Songti.ttc')
ax.set_yticklabels(name)

plt.show()
