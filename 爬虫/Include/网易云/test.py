#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
AES加密解密工具类
@author jzx
@date   2018/10/24
此工具类加密解密结果与 http://tool.chacuo.net/cryptaes 结果一致
数据块128位
key 为16位
iv 为16位，且与key相等
字符集utf-8
输出为base64
AES加密模式 为cbc
填充 pkcs7padding
"""

import base64
from Crypto.Cipher import AES

import random


def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    """
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return:
    """
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


def encrypt(key, content):
    """
    AES加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = bytes('0102030405060708', encoding='utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result


def decrypt(key, content):
    """
    AES解密
     key,iv使用同一个
    模式cbc
    去填充pkcs7
    :param key:
    :param content:
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # base64解码
    encrypt_bytes = base64.b64decode(content)
    # 解密
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    # 重新编码
    result = str(decrypt_bytes, encoding='utf-8')
    # 去除填充内容
    result = pkcs7unpadding(result)
    return result


def get_key(n):
    """
    获取密钥 n 密钥长度
    :return:
    """
    c_length = int(n)
    source = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    length = len(source) - 1
    result = ''
    for i in range(c_length):
        result += source[random.randint(0, length)]
    return result


# Test
# 非16字节的情况
aes_key = get_key(16)
aes_key='0CoJUm6Qyw8W8jud'
print('aes_key:' + aes_key)
# 对英文加密
source_en = '{"rid":"R_SO_4_1363205817","offset":"40","total":"false","limit":"20","csrf_token":""}'
encrypt_en = encrypt(aes_key, source_en)
print(encrypt_en)
# 解密
decrypt_en = decrypt(aes_key, encrypt_en)
print(decrypt_en)
print(source_en == decrypt_en)
# 中英文混合加密
# source_mixed = 'Hello, big赛赛'
# encrypt_mixed = encrypt(aes_key, source_mixed)
# print(encrypt_mixed)
# decrypt_mixed = decrypt(aes_key, encrypt_mixed)
# print(decrypt_mixed)
# print(decrypt_mixed == source_mixed)
#
# # 刚好16字节的情况
# en_16 = 'abcdefgj10124567'
# encrypt_en = encrypt(aes_key, en_16)
# print(encrypt_en)
# # 解密
# decrypt_en = decrypt(aes_key, encrypt_en)
# print(decrypt_en)
# print(en_16 == decrypt_en)
# mix_16 = 'abx张三丰12sa'
# encrypt_mixed = encrypt(aes_key, mix_16)
# print(encrypt_mixed)
# decrypt_mixed = decrypt(aes_key, encrypt_mixed)
# print(decrypt_mixed)
# print(decrypt_mixed == mix_16)
