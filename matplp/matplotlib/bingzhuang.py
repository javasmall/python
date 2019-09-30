# -*- coding: utf-8 -*

from matplotlib.font_manager import FontManager, FontProperties
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 使用Mac系统自带的中问字体
# def getChineseFont():
#     return FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')


# 设置图片大小
# plt.figure(figsize=(9,6))
label = u'超载', u'船员责任心不强', u'船员驾驶技术太差', u'通航环境差', u'海事、港航监管不到位', u'船舶过于老旧', u'冒险航行'  # 各类别标签
color = 'red', 'orange', 'yellow', 'green', 'blue', 'gray', 'goldenrod'  # 各类别颜色
size = [34, 5, 6, 14, 1, 10, 23]  # 各类别占比
explode = (0.2, 0, 0, 0, 0, 0, 0)  # 各类别的偏移半径

# plt.subplot(2,3,1)
# 绘制饼状图
pie = plt.pie(size, colors=color, explode=explode, labels=label, shadow=True, autopct='%1.1f%%')
# 饼状图呈正圆
for font in pie[1]:

    font.set_size(8)
for digit in pie[2]:
    digit.set_size(8)

plt.axis('equal')
plt.title(u'你认为砂石船发生事故的主要原因在于', fontsize=12)

plt.legend( loc=0, bbox_to_anchor=(0.82, 1))  # 图例
# 设置legend的字体大小
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=6)

# 显示图
plt.show()