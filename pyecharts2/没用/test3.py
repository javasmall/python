# 加载pyecharts
from pyecharts import Geo, Style
import pandas as pd

# 导入excel表举例
df = pd.read_excel('流动人口.xlsx')
df.head()

# 导入自定义的地点经纬度
geo_cities_coords = {df.iloc[i]['地点']: [df.iloc[i]['经度'], df.iloc[i]['纬度']]
                     for i in range(len(df))}  # 根据文件大小生成字典
attr = list(df['地点'])  # 字典的每个键值
value = list(df['流动人口'] / 100000)  # 由于量值的太大，换算以下(散点的颜色就是和这个想关的)
style = Style(title_color="#fff", title_pos="center",
              width=1200, height=600, background_color="#404a59")

# 可视化
geo = Geo('东莞各个CGI总用户数分布', **style.init_style)
geo.add("", attr, value, visual_range=[0, 100], symbol_size=5,
        visual_text_color="#fff", is_piecewise=True,
        is_visualmap=True, maptype='东莞', visual_split_number=10,
        geo_cities_coords=geo_cities_coords)

geo.render('东莞各个CGI总用户数分布.html')