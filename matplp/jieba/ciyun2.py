# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba.analyse

txt1="  随着移动互联网的潮流，越来越多的工厂、公司已经借助于互联网的各种优势实现了工厂和公司的信息化生产和信息化管理，从而获得了比较好的效益。但是我们发现，在初中和高中校园里互联网技术对于中学校园中的考试(错题、批改试卷、成绩可视化分析)这一块儿的改善并没有那么明显或者说普及程度没有那么高。" \
     "本项目以智慧决策应用为驱动，以智能、美观的数据展示为开发目标，通过研究可视化建模、多表联动、数据大屏、主题模板等技术，设计并实现用户可定制的、基于云的数据可视化平台，从而提升决策的科学性与准确性。"
ags = jieba.analyse.extract_tags(txt1, topK=30)#jieba分词关键词提取，40个
print(ags)
text = " ".join(ags)
text="快速分析—持久储存 细致图表—比分数告诉你的更多  分析报告—用数据告诉你的状态 错题题库—精准拍搜 人工智能—回归预测 移动pc—随时随地"
print(text)
#backgroud_Image = plt.imread('tt.jpg')#如果需要个性化词云
wc = WordCloud(background_color="white",
               width=1500, height=1200,
               #mask=backgroud_Image,  # 设置背景图片

                min_font_size=50,
               font_path="simhei.ttf",
               max_font_size = 200,  # 设置字体最大值
               random_state=29,  # 设置有多少种随机生成状态，即有多少种配色方案
               )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
# wc.font_path="simhei.ttf"
my_wordcloud = wc.generate(text)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()#如果展示的话需要一个个点
file='image/'+str("jishu")+'.png'
wc.to_file(file)

