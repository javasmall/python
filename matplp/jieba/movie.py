import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba.analyse
import pymysql
db = pymysql.connect(host="biggsai.com", user="root",
                     password="123456", db="project", port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()

def savatofile(name,txt1):
    ags = jieba.analyse.extract_tags(txt1, topK=40)#jieba分词关键词提取，40个
    text = " ".join(ags)
    backgroud_Image = plt.imread('tt.jpg')#如果需要个性化词云
    wc = WordCloud(background_color="white",
                   width=900, height=600,
                   mask=backgroud_Image,  # 设置背景图片

                   #min_font_size=30,
                   font_path="simhei.ttf",
                    #max_font_size = 260,  # 设置字体最大值
                   random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )  # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
    # wc.font_path="simhei.ttf"
    my_wordcloud = wc.generate(text)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    #plt.show()#如果展示的话需要一个个点
    file='image/'+str(name)+'.png'

    wc.to_file(file)  # 保存图片文件
#从数据库提取文本
sql="select * from ciyun"
cur.execute(sql)
value=cur.fetchall()
for q in value:
    name=q[0]
    text=q[2]
    try:
       savatofile(name,text)
    except Exception as e:
       print(e)
# txt1 = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门，午门居中向阳。"
# savatofile('bigsai',txt1)
#txt1 = open('word.txt', 'r', encoding='utf8').read()    # word.txt，随便放点中文文章
# words_ls = jieba.cut(txt1, cut_all=False)
# words_split = " ".join(words_ls)

