import re
from snownlp import SnowNLP
import numpy as np
import matplotlib.pyplot as plt  ##绘图库
from wordcloud import WordCloud
import jieba.analyse
time=[]#次数
text=[]#文本
name=[]#姓名
qq=[]#qq或者邮箱提取
value={}
pattern=re.compile(r'(\d*)-(\d*)-(\d*) .* .*')#匹配   2018-05-05 15:55:40 2班某某(1315426911) 有一个坑点就是2018-05-07 13:48:39 2XXX<xxxx@qq.com>这种格式
#pattern2=re.compile(r'(\d+):(\d+):\d+')#匹配 15:55:40
pattern3=re.compile(r'(\S+)(\()(.*?)(\))')#匹配    2班某某(1315426911)相关内容
pattern4=re.compile(r'(\S+)[<](.*)[>]')
def getemotionbyqq(value,qq):#获取qq的该学生的情感信息
    va=value[qq]['text']
    emotion=[]
    for q in va[0:len(va)]:
        s = SnowNLP(q)
        emotion.append(s.sentiments)
        #print(s.sentiments)
    x=np.arange(len(emotion))
    y=np.array(emotion)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(12, 6))  ##指定图像比例： 8：6
    plt.plot(x,y,label='emotion status')
    plt.xlabel("最近n次发言情绪走势")
    plt.ylabel("0-1表示消极-积极")
    plt.legend()
    plt.savefig("img/%semotion.png"%(qq))
    #plt.show()
def getstudentcloudbyqq(value,qq):#获取学生的词云
    va=value[qq]['text']
    text=''
    for q in va:
        text+=q+' '
    print(text)
    ags = jieba.analyse.extract_tags(text, topK=40)
    text=' '.join(ags)
    wc = WordCloud(background_color="white",
                   width=900, height=600,
                  # min_font_size=40,
                   font_path="simhei.ttf",
                   #max_font_size=300,  # 设置字体最大值
                   random_state=40,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
    # wc.font_path="simhei.ttf"
    my_wordcloud = wc.generate(text)

    my_wordcloud.to_file("img/%scloud.png"%(qq))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    #plt.show()
    plt.close()
def getemotionall(time,text,name,qq):
    emotion=[]
    for i in range(0,len(qq)):
       # print(name[qq[i]],text[i])
        va=0
        for j in value[str(qq[i])]['text']:
            s=SnowNLP(j)
            va+=s.sentiments*100
        emotion.append(va/(0.1+len(value[qq[i]]['text'])))#防止/0
    print(len(name),len(emotion))
    Xi = np.array(emotion[43:84])
    Yi = np.array(name[43:84])
    x = np.arange(0, 41, 1)
    width = 0.6
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(10, 8))  ##指定图像比例： 8：6
    plt.barh(x, Xi, width, color='red',label='同学发言总情绪', alpha=0.8)
    plt.xlabel("emotion")
    plt.ylabel("name")
    for a, b, c in zip(Xi, Yi, x):
        print(a, b, c)
        plt.text(a + 2, c - 0.4, '%d' % int(a), ha='center', va='bottom')
    plt.yticks(x, Yi)
    plt.xlim(0,100)
    # plt.legend()
    plt.savefig("emotion2.png")
    plt.show()
    plt.close()
#展示各个同学的发言次数
def getspeaktimeall(time,name):
    Xi = np.array(time[43:84])#根据自己展示的需要需改范围，我们群人数太多
    Yi = np.array(name[43:84])
    x=np.arange(0,41,1)
    width=0.6
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(10, 8))  ##指定图像比例： 8：6
    plt.barh(x , Xi, width, color='SkyBlue',alpha=0.8)
    plt.xlabel("time")
    plt.ylabel("name")
    for a,b,c in zip(Xi,Yi,x):
        print(a,b,c)
        plt.text(a+10,c-0.4,'%d'%int(a),ha='center',va='bottom')
    plt.yticks(x,Yi)
   # plt.legend()
    plt.savefig("wordtime2.png")
    plt.show()
    plt.close()

def getmotion(values):
    for key in values:
        print(values[key])
        time.append(values[key]['text'].__len__())
        usertxt=''
        for txt in values[key]['text']:
            usertxt+=txt+' '
        text.append(usertxt)
        name.append(values[key]['name'])
        qq.append(key)
    #getmatplotlibtime(time,text,name,qq)
   # getmatplotlibemotion(time,text,name,qq)
   # print(time)
def analyseinformation(lines):
    qqnow=''#qq或者email当前用户
    for line in lines:
        if line != "\n" and line.strip() != "\n" and line != None and not line.__contains__("撤回了"):
           line = line.replace("[表情]", " ").replace("@全体成员", " ").replace("[表情]", " ").\
                replace("[QQ红包]我发了一个“专享红包”，请使用新版手机QQ查收红。", "").replace("\n", " ").replace("[图片]",'')
           if pattern.search(line):#匹配到正确的对象
               # print(line)
                if pattern3.search(line):
                    qq1=str(pattern3.search(line).group(3))
                    namenow=str(pattern3.search(line).group(1))
                    if  not qq1 in value.keys():
                         value[qq1]={'name':namenow,'qq':qq1,'text':[]}
                    qqnow=qq1#当前用户发言发生了更改
                elif pattern4.search(line):
                    email=str(pattern4.search(line).group(2))
                    namenow=str(pattern4.search(line).group(1))
                    if  not email in value.keys():
                         value[email]={'name':namenow,'qq': email,'text':[]}
                    qqnow=email
               # print(name)
           elif not qqnow.__eq__(''):#初始化的时候的坑，初始化为'',前几行没用文本直接过滤
                value[qqnow]['text'].append(str(line))
               # print(name)
                #print(value[name])
if __name__ == '__main__':
    f = open('./img/tex.txt', 'r', encoding='utf-8')  # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
    lines = f.readlines()
    #执行这个函数获取分析才能解析value{}
    analyseinformation(lines)
    getmotion(value)#这个函数获取一些name[]数组的值
    #核心分析函数：

    print(len(name),len(time))
    getspeaktimeall(time,name)#选定区间的同学发言次数
    getemotionall(time,text,name,qq)
    for q in qq:#每个同学的
        try:
            getstudentcloudbyqq(value,q)
            getemotionbyqq(value,q)
        except Exception as e:
            print(e)
            





