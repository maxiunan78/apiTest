#!/usr/bin/env python
#-*- coding:utf-8 -*-

#author:maxiunan

import pyexcel as p



class Helper(object):
    """公共方法"""
    def readExcel(self,excelPath,sheet_name,start_row=0,start_column=0):
        dict_records = p.get_dict(file_name=excelPath, sheet_name=sheet_name, start_row=start_row,
                                   start_column=start_column, skip_empty_rows=True,
                                   skip_empty_coloums=True)
        # sheet_records.name_columns_by_row(0)
        # dict_records = sheet_records.to_dict()
        # print(dict_records)
        return dict_records

    def get_caseData(self,dict_records,titleName,rowIndex):
        """获取请求地址"""
        return dict_records[titleName][rowIndex]
# if __name__ == '__main__':
   # dict_records = Helper().readExcel(excelPath=excelPath,sheet_name='recharge')
   # print(Helper().get_caseData(dict_records=dict_records,titleName='url',rowIndex=0))

