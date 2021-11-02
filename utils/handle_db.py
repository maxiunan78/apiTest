#!/usr/bin/env python
#-*- coding:utf-8 -*- 

#author:maxiunan

import pymysql

class DbHandler:

    def __init__(self,host,port,user,password,database,charset,**kwargs):

        self.conn = pymysql.connect(host=host,port=port,user=user,password=password,database=database,
                                    cursorclass=pymysql.cursors.DictCursor,charset=charset,**kwargs)

        self.cursor = self.conn.cursor()


    def query(self,sql,args=None,one=True):
        self.cursor.execute(sql,args)
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return  self.cursor.fetchall()

    def clse(self):
        self.cursor.close()
        self.conn.close()

if __name__=="__main__":
    db = DbHandler(host='',port='',user='',password='',database='',charset='utf8')
    sql = 'select * from user limit 1;'
    data = db.query(sql)
    print(data)
