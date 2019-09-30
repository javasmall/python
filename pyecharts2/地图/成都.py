from pyecharts import Geo, Page, Style
from pyecharts import Bar
import  csv
import random

def addpoint(cvsname,weight):
    csv_file=csv.reader(open('chengdu1.csv','r'))
    index=[]
    jingdu=[]
    weidu=[]
    data={}
    print(data)
    for line in csv_file:
        print(line)
        print(line[1])
        try:
            # index.append(line[0])
            # jingdu.append(line[2])
            # weidu.append(line[3])
            # if(int(int(line[0])<1000)):
             data[line[1]]=[float(line[2]),float(line[3])]
             geo.add_coordinate(line[0],float(line[2]),float(line[3]))
             weight2=5

             list.append((line[0],weight2))
        except Exception as e:
            print(e)
list=[]
geo = Geo(
    "成都出租车分布",
    "Taxi Distribution in ChengDu",
    title_color="red",
    title_pos="center",
    width=1000,
    height=600,
    background_color="#F0F8FF",  ##背景色

)
addpoint('',5)
attr, value = geo.cast(list)
style = Style(title_color= "#fff",title_pos = "center",
width = 1200,height = 600,background_color = "#404a59")

geo.add(
    "",
    attr,
    value,
    visual_range=[0,24],
    maptype='成都',
    visual_text_color="black",
    geo_normal_color="#fff",#省市块颜色
    symbol_size=2,
    is_visualmap=True,
    is_piecewise=True,
    visual_split_number=4,
    tooltip_background_color="black"
)
geo.render()
