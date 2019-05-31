import numpy as np
import  pandas as pd
import xlwt
import xlrd
data = xlrd.open_workbook('2019-51MCM-Problem C-Appendix 2.xlsx') # 打开xls文件

value={}
print(value)
for i in range(10):

    table= data.sheets()[i] # 打开第i张表
    value[str(i)]=[]
    #print(table.row_values(4))
    for j in range(2,2721):
        value[str(i)].append(table.row_values(j))
   ## value[i]={}

for i in range(10):
    value[str(i)].sort(key=lambda x:x[0],reverse=False)
    #print(value[str(i)][0])
#print(value[str(0)])
for j in range(2719):
    print(value[str(0)][j])

w=xlwt.Workbook(encoding = 'ascii')
for i in range(10):
    year=str(2018-i)
    ws=w.add_sheet(year)
    for j in range(2,2721):
        for q in range(10):
            try:
             ws.write(j,q,value[str(i)][j][q])
            except Exception as e:
                continue
            #print(value[str(i)][j][q])
            #continue
w.save("sort2.xls")
