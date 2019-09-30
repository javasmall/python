import  csv
import random
import pandas as pd
csv_file=csv.reader(open('到港时间.csv','r'))

time=[]
count=[]
hangban=[]
chuzuche=[]
houche=[]#候车时间
shangche=[]
distance=[]
minite=[]
index=0
for va in csv_file:

    if index==0 :
        index+=1
        continue
    try:
        index+=1
        time.append(va[0])
        count.append(va[1])
        hangban.append(va[2])
        chuzuche.append(va[3])
        houche2=(30/int(va[1]))+(30/int(va[3]))+(20/int(va[1]))*(20/int(va[3]))
        houche.append(houche2)
        shangche2=random.randint(1,2)+random.randint(1,2)
        shangche.append(shangche2)
        distance2=5+random.randint(-4,3)+random.randint(0,1)+random.randint(0,2)
        money=int(distance2)*2.4+8
        distance.append(money)
        min=random.randint(0,1)+1+random.randint(0,2)
        minite.append(min)
        print(va[0],houche2,shangche2,money)#候车时间，上车时间，前
        #print(distance)
    except Exception as  e:
        print(e)
# 字典中的key值即为csv中列名
print(len(time),len(houche))
dataframe = pd.DataFrame({'时间点':time , '候车时间': houche,'到港航班':hangban,'出租车数量':chuzuche,'钱':distance,'上车时间花费':shangche})
#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("凑数据.csv",index=False,sep=',')