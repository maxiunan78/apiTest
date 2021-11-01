#!/usr/bin/env python
#-*- coding:utf-8 -*-

#author:maxiunan
import hashlib

def sortKeys(param):
    # print(sorted(param.items()))
    return dict(sorted(param.items()))


def md5_key(arg):
    hash = hashlib.md5()
    hash.update(arg.encode(encoding='utf-8'))
    return hash.hexdigest().upper()

def get_signStr(sortedData,app_key):
    result = ''
    for key,val in sortedData.items():
        if val != '':
            result = result + key +str(val)
    # print("result:"+ result)
    sinStr = app_key + result + app_key
    # print(sinStr)
    return sinStr

#
# if  __name__ == '__main__':
#
#     print(app_sign)
