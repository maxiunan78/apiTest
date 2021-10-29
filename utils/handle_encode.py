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
    return hash.hexdigest()

def get_signStr(sortedData,app_key):
    result = ''
    for key,val in sortedData.items():
        result = result + key +val
    # print("result:"+ result)
    sinStr = app_key + result + app_key
    print(sinStr)
    return sinStr


if  __name__ == '__main__':
    appId = '17442'
    app_key = '86079af0-ef2b-4b55-b8a0-8d29f4e15379'
    rowData = {'appId':appId,
               'app_key':app_key,
               'timestamp':'2016-01-01 12:00:00',
               'signMethod': 'md5',
               'memberId':'12123'
               }
    sortedData = sortKeys(rowData)
    app_sign = md5_key(get_signStr(sortedData,app_key))
    print(app_sign)
