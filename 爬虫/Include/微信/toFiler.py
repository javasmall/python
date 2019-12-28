import itchat
itchat.auto_login(hotReload=True)
# friends=itchat.search_friends("18796011370")
# print(friends[0])
# username=friends[0]['UserName']
# itchat.send('Hello, filehelper,54bigsai', toUserName=username)

# isGroupChat=True表示为群聊消息
#@itchat.msg_register([TEXT, SHARING], isGroupChat=True)

# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 返回信息调用信息
    text=msg['Text']
    print(text,msg)
    itchat.send('可以', toUserName=msg['ToUserName'])
    return msg['Text']

# 绑定消息响应事件后，让itchat运行起来，监听消息
itchat.run()