def abc():
    print('jjj')
    print(88888)
abc()
def add(a,b):
    c=a+b;
    print(c)
add('afsa','fa')

def add2(a,b,c):
    print(a,b,c)
add2(3,999,888)

def printline():
    print('-'*30)
printline()

q=1
q=int(q)
def adda():
    global  q#添加glabol之后才可以
    #q=50
    q+=20
adda()
print(q)


def retutnmore(a,b):#python函数可以返回多个值
    return b,a
a=1000
b=100
a,b=retutnmore(a,b)
print(a,b)
#缺省参数
def printinfo( name, age = 35 ):
   # 打印任何传入的字符串
   print( "Name: ", name)
   print ("Age ", age)

# 调用printinfo函数
printinfo(name="miki" )
printinfo( age=9,name="miki" )

def jiecheng(a):
    if a==1:
        return a
    else:return  a*jiecheng(a-1)
print(jiecheng(4))

stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
stus.sort(key=lambda x:x['age'])
print(stus)

