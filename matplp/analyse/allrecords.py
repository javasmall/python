import re
import numpy as np
import matplotlib.pyplot as plt  ##绘图库
from wordcloud import WordCloud
import jieba.analyse
string="2018-05-05 15:55:40 2班某某(1315426911)"
pattern=re.compile(r'(\d*)-(\d*)-(\d*) .* .*')#匹配   2018-05-05 15:55:40 2班某某(1315426911) 有一个坑点就是2018-05-07 13:48:39 2XXX<xxxx@qq.com>这种格式
pattern2=re.compile(r'(\d+):(\d+):\d+')#匹配 15:55:40
pattern3=re.compile(r'(\()(.*?)(\))')#匹配    2班某某(1315426911)相关内容
pattern4=re.compile(r'(\S+)[<].*[>]')
f = open('./img/tex.txt', 'r', encoding='utf-8')  # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
lines = f.readlines()
index=0
def getpicture(y):#matplotlib绘图 发言分布
    x=[]
    for i in range(0,24):
        x.append(str(i)+':00-'+str(i+1)+':00')
    Xi = np.array(x)
    Yi = np.array(y)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
    plt.subplots_adjust(bottom=0.2)
    plt.scatter(Xi, Yi, color="red", label="times")
    plt.xlabel("时间00：00—24：00")
    plt.ylabel("发言次数/次")
    plt.xticks(range(0,24),rotation=75,fontsize=10)#设置横坐标显示24次。
    plt.yticks(range(0,1000,50))
   # plt.legend(loc='lower right')  # 绘制图例
   # plt.show()
    plt.savefig("hour.png",format='png')
    plt.close()
def getciyun(value):
    text=''
    for i in range(0,24):
        text+=str(value[i]['text'])
    args=jieba.analyse.extract_tags(text,topK=80)
    text=' '.join(args)
    wc = WordCloud(background_color="white",
                   width=1200, height=900,
                   #min_font_size=40,
                   font_path="simhei.ttf",
                  # max_font_size=300,  # 设置字体最大值
                   #random_state=40,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
    # wc.font_path="simhei.ttf"
    my_wordcloud = wc.generate(text)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    wc.to_file('wordcloud.png')
def analysebyhour(lines):
    value=[]
    y=[]
    index=0
    for i in range(0,24):
        value.append({})
        value[i]['time']=0
        value[i]['text']=''
    for line in lines:
        if line != "\n" and line.strip() != "\n" and line != None and not line.__contains__("撤回了"):
           line = line.replace("[表情]", " ").replace("@全体成员", " ").replace("[表情]", " ").\
                replace("[QQ红包]我发了一个“专享红包”，请使用新版手机QQ查收红。", "").replace("\n", " ").replace("[图片]",'')
           if(pattern.search(line)):#匹配到正确的对象
                date=pattern.search(line)
                hour=pattern2.search(line).group(1)
                #print(date.group(0),hour)
                value[int(hour)]['time']+=1
                index=hour
           else:
               print(line)
               value[int(index)]['text']+=str(line)
    for i in range(0,24):
        print('time:',i,'time',value[i]['time'])
        y.append(value[i]['time'])
    getpicture(y)
    getciyun(value)
analysebyhour(lines)


