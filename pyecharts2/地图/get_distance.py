import  csv
from geopy.distance import geodesic
import datetime
import pandas as pd
print(geodesic((30.28708,120.12802999999997), (28.7427,115.86572000000001)).m) #计算两个坐标直线距离
print(geodesic((30.28708,120.12802999999997), (28.7427,115.86572000000001)).km) #计算两个坐标直线距离


csv_file=csv.reader(open('滴滴数据.csv','r'))
id=[]
distance=[]
time_all=[]
speed=[]
starttime=[]
for line in csv_file:
    print(line)
    try:
        userid=line[0]
        p1=str(line[2])
        p2=str(line[3])
        a1=(float(p1.split(",")[1]),122)
        a2 = (float(p2.split(",")[1]),122)
        a3=(0,float(p1.split(",")[0]))
        a4=(0,float(p2.split(",")[0]))
        p_distance=geodesic(a1, a2).km+geodesic(a3,a4).km
        time1=line[6]
        time2=line[7]
        datetime1 = datetime.datetime.strptime(time1, '%Y/%m/%d %H:%M')
        datetime2 = datetime.datetime.strptime(time2, '%Y/%m/%d %H:%M')
        time=(datetime2-datetime1).seconds/60
        v = float(p_distance) / (float(time) + 0.1) *60
        id.append(userid)
        distance.append(p_distance)
        time_all.append(time)
        starttime.append(datetime1.hour+datetime1.minute/60)

        speed.append(v)
    except Exception as  e:
        print(e)
print(id)
print(distance)
print(time_all)
print(len(speed),len(distance))
# 字典中的key值即为csv中列名
dataframe = pd.DataFrame({'userid':id , 'distance(km)': distance,'time(min)':time_all,'speed':speed,'starttime':starttime})
#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("滴滴数据计算.csv",index=False,sep=',')


# 将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("test.csv", index=False, sep=',')
