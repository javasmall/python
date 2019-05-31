import pymysql  # 导入 pymysql

# 打开数据库连接
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456", db="car", port=3306)
#
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
# # 编写sql 查询语句  user 对应我的表名
# sql="insert into sheng(sheng_name,sheng_url,place_id) values('北京','http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10065.html',10065)"
# try:
#     cur.execute(sql)  # 执行sql语句
#
#     db.commit()
# except Exception as e:
#     print(e)
# finally:
#     db.close()  # 关闭连接
