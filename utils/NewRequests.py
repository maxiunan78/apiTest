#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests

class RequestHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self,method,url,params=None, data=None, json=None, headers=None, **kwargs):
        return  self.session.request(method, url, params=params,data=data,json=json,headers=headers,**kwargs )

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