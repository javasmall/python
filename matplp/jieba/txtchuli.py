# -*- coding: utf-8 -*-
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import jieba.analyse
# plt.rcParams['font.family'] = ['Droid Sans Fallback']
# plt.rcParams['axes.unicode_minus'] = False
coding = 'utf-8'
pattern=re.compile(r'\d*-\d*-\d*.* \d*')
pattern2=re.compile(r'(\()(.*?)(\))')

txt1=''

f = open('../analyse/img/text.txt', 'r',encoding='utf-8')  # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
lines = f.readlines()
index=0
for line in lines:

 if line !="\n" and line.strip() !="\n" and line!=None and not line.__eq__('[图片]\n')\
         and not line.__eq__("[表情]\n")and not line.__eq__("[QQ红包]我发了一个“专享红包”，请使用新版手机QQ查收红。\n"):
    index+=1
    #print(index," index:",line,end="")
    try:
     if(not pattern.search(str(line))):
        txt1 += line
    except Exception as  e:
        print(index,e)
    #      print(pattern.search(str(line)).group())



#print(txt1,end="")
words_ls = jieba.cut(txt1, cut_all=False)
words_split = " ".join(words_ls)
ags = jieba.analyse.extract_tags(txt1, topK=80)
text=" ".join(ags)
print(words_split)
wc = WordCloud(background_color="white",
               width=1500,height=1000,
               min_font_size=40,
               font_path="simhei.ttf",
               max_font_size = 300,  # 设置字体最大值
               random_state = 40,  # 设置有多少种随机生成状态，即有多少种配色方案
)    # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
#wc.font_path="simhei.ttf"
my_wordcloud = wc.generate(text)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
wc.to_file('zz.png')



