# -*- coding: utf-8 -*-
import itchat
import pandas as pd
import openpyxl

itchat.auto_login(True)
friendList = itchat.get_friends(update = True)

dfd = pd.DataFrame(friendList)
dfd.to_excel('wechat.xlsx')