#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import handle_encode as ha
import json
#
# openApi 测试环境
openApiUrl = "https://openapi.test.youzhanguanjia.com"

class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()
        self.baseUrl = openApiUrl

    def visit(self,method,url,params=None, data=None,headers=None, **kwargs):
        self.url = self.baseUrl + url
        return  self.session.request(method, self.url, params=params,data=json.dumps(data,sort_keys=True,separators=(',', ':')),headers=headers,**kwargs )

    def close_session(self):
        """关闭session"""
        self.session.close()

# if __name__ == '__main__':
#     url = 'https://uat-new-hybman.jhjbxj.com/user/login'
#     data = {
#         "channelCode":"JHJHOME",
#         "passport":"admin",
#         "passwd":"e3ceb5881a0a1fdaad01296d7554868d"
#     }
#     req = RequestHandler()
#     login_res = req.visit("post",url,data=data)
#     print(login_res.text)

if __name__ == '__main__':

    # 新增会员
    # url = '/openapi/member/addMember'
    # appId = '10001'
    # app_key = "asdfasdf34123"
    #
    #
    # rowData =\
    #     {
    #     "appId":"10001",
    #     "app_key":"10001",
    #     "timestamp":"2018-11-01 16:00:00",
    #     "signMethod": "md5",
    #     "stationId": "165481001",
    #     "memberName": "马锈南",
    #     "phoneNum": "13882130978",
    #     "idCard": "510781199511021111",
    #     "isCheckFuellingPw": "1",
    #     "fuellingPassword": "123456",
    #     "isCheckLicensePlate": "0",
    #     "licensePlate": "川A25487",
    #     "memo": "备注",
    #     "hqId": "16548",
    #     "recommendId": "",
    #     "stationAdminId": "1654810000169",   # 操作员
    #     "hqMemberGradeId": "674",
    #     "cardNo": "813500705"
    #     }
    #



    url = '/openapi/trade/selfPay'
    appId = '10001'
    app_key = "asdfasdf34123"

    rowData = \
        {
            "appId": "10001",
            "app_key": "10001",
            "hqId":"16548",
            "timestamp": "2020-11-01 16:00:00",
            "signMethod": "md5",
            "stationId": "165481001",
            "stationName": "油掌柜测试站",
            "orderId": "dsfddh13882130978",
            "fpId": "16548106001",
            "fpNo": "1",
            "prId":"2",
            "prName":"93#汽油",
            "price":"7.5",
            "vol":"3",
            "receivableAmount":"60",
            "discountAmount":"5",
            "realincomeAmount":"55",
            "memberDiscounts":"1",
            "couponDiscounts":"3",
            "activityDiscounts":1,
            "thirdMemberId":"42342423",
            "yzgMemberId":"64190"

        }

    sortedData = ha.sortKeys(rowData)
    print(sortedData)
    app_sign = ha.md5_key(ha.get_signStr(sortedData, app_key))
    # print(app_sign)
    add_dict = {"app_sign": app_sign}
    # print(add_dict)
    rowData.update(add_dict)
    payload = rowData
    # print(payload)
    req = RequestHandler()
    login_res = req.visit("post", url, data=payload, headers={'Content-Type': 'application/json'})
    print(login_res.text)

    req.close_session()
