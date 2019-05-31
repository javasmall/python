import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba.analyse
txt1 = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门，午门居中向阳。"
#txt1 = open('word.txt', 'r', encoding='utf8').read()    # word.txt，随便放点中文文章
#words_ls = jieba.cut(txt1, cut_all=False)
#words_split = " ".join(words_ls)
ags = jieba.analyse.extract_tags(txt1, topK=10)
text=" ".join(ags)
print(text)
#print(words_split)
wc = WordCloud(background_color="white",
               width=1000,height=600,
               min_font_size=20,
               font_path="simhei.ttf",
               #max_font_size = 200,  # 设置字体最大值
               random_state = 30,  # 设置有多少种随机生成状态，即有多少种配色方案
)    # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
#wc.font_path="simhei.ttf"
my_wordcloud = wc.generate(text)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

wc.to_file('zzz.png') # 保存图片文件