#!/usr/bin/env python
#-*- coding:utf-8 -*- 

#author:maxiunan

import unittest
from  utils.NewRequests import RequestHandler

class Api(unittest.TestCase):
    def statusCode(self,r):
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.status_code,200)

    # def test_api_001(self):
    #     """登录系统"""
    #     url = 'https://uat-new-hybman.jhjbxj.com/user/login'
    #     data = {
    #         "channelCode":"JHJHOME",
    #         "passport":"admin",
    #         "passwd":"e3ceb5881a0a1fdaad01296d7554868d"
    #     }
    #     req = RequestHandler()
    #     login_res = req.visit("post",url,data=data)
    #     self.statusCode(r=login_res)
    #     with open('token','w') as f:
    #         f.write(login_res.json()['data']['token'])

    def getToken(self):
        """读取token文件内容"""
        with open('token','r') as f:
            return f.read()

if __name__ == '__main__':
    unittest.main(verbosity=2)