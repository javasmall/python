from multiprocessing import Pool 
from time import sleep,ctime 

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池
pool = Pool(processes = 4)

result = []
for i in range(10):
    msg = "hello %d"%i
    #将事件放入进程池队列,等待执行
    r = pool.apply_async(func = worker,args = (msg,))
    result.append(r)

#关闭进程池
pool.close()

#回收
pool.join()

for i in result:
    print(i.get())  #获取事件函数的返回值
