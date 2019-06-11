import json
import chardet


listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)
dictStr = {"city": "北京", "name": "大猫"}
# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
# chardet.detect()返回字典, 其中confidence是检测精确度

print(json.dumps(listStr))
# '[1, 2, 3, 4]'
print(json.dumps(tupleStr))
# '[1, 2, 3, 4]'
#转换成json对象
q=json.dumps(dictStr)
print(q)

#json转换成python对象
print(json.loads(q))
# {'confidence': 1.0, 'encoding': 'ascii'}

# print(json.dumps(dictStr, ensure_ascii=False))
# # {"city": "北京", "name": "大刘"}
#
# chardet.detect(json.dumps(dictStr, ensure_ascii=False))
# # {'confidence': 0.99, 'encoding': 'utf-8'}