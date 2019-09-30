import matplotlib.pyplot as plt
import matplotlib
import jieba
import  jieba.analyse
import xlwt
import xlrd
from wordcloud import WordCloud
import numpy as np
from collections import Counter
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

def anylasescore(comment):
    score=[0,0,0,0,0,0]
    count=0
    for va in comment:
        try:
            score[int(va[2])]+=1
            count+=1
        except Exception as e:
            continue
    print(score)
    label='1分','2分','3分','4分','5分'
    color = 'blue', 'orange', 'yellow', 'green', 'red'  # 各类别颜色
    size=[0,0,0,0,0]
    explode=[0,0,0,0,0]
    for i in range(1,5):
        size[i]=score[i]*100/count
        explode[i]=score[i]/count/10
    pie = plt.pie(size, colors=color, explode=explode, labels=label, shadow=True, autopct='%1.1f%%')
    for font in pie[1]:
        font.set_size(8)
    for digit in pie[2]:
        digit.set_size(8)
    plt.axis('equal')
    plt.title(u'各个评分占比', fontsize=12)
    plt.legend(loc=0, bbox_to_anchor=(0.82, 1))  # 图例
    # 设置legend的字体大小
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=6)
    plt.savefig("score.png")
    # 显示图
    plt.show()
def getzhifang(map):
    x=[]
    y=[]
    for k,v in map.most_common(15):
        x.append(k)
        y.append(v)
    Xi = np.array(x)
    Yi = np.array(y)
    x = np.arange(0, 15, 1)
    width = 0.6
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
    plt.bar(Xi, Yi, width, color='blue', label='热门词频统计', alpha=0.8,)

    plt.xlabel("词频")
    plt.ylabel("次数")
    plt.show()
    return
def getciyun_most(map):
    x = []
    y = []
    for k, v in map.most_common(300):
        x.append(k)
        y.append(v)
    xi=x[0:150]
    xi=' '.join(xi)
    print(xi)
    backgroud_Image = plt.imread('nezha.jpg')  # 如果需要个性化词云
    wc = WordCloud(background_color="white",
                   width=1500, height=1200,
                   #min_font_size=40,
                   mask=backgroud_Image,
                   font_path="simhei.ttf",
                   max_font_size=150,  # 设置字体最大值
                   random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
    # wc.font_path="simhei.ttf"
    my_wordcloud = wc.generate(xi)
    plt.imshow(my_wordcloud)
    my_wordcloud.to_file("img.jpg")
    xi=' '.join(x[150:300])
    my_wordcloud = wc.generate(xi)
    my_wordcloud.to_file("img2.jpg")

    plt.axis("off")

def anylaseword(comment):
    list=['这个','一个','不少','起来','没有','就是','不是','那个','还是','剧情','这样','那样','这种','那种','故事','人物','什么']
    list.append("这个")
    print(list)
    commnetstr=''
    c = Counter()
    low=Counter()
    index=0
    for va in comment:
        seg_list = jieba.cut(va[3],cut_all=False)
        index+=1
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':
                 try:
                    c[x]+=1
                 except:
                     continue
        commnetstr+=va[3]
    for (k, v) in c.most_common():
        if v<5 or k in list:
            c.pop(k)
            continue
        #print(k,v)
    print(len(c),c)
    getzhifang(c)
    getciyun_most(c)
    #print(commnetstr)
def anylase():
    data = xlrd.open_workbook('nezha.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第i张表
    comment = []
    for i in range(1, 500):
        comment.append(table.row_values(i))
    # print(comment)
    anylasescore(comment)
    anylaseword(comment)

if __name__ == '__main__':
    anylase()

