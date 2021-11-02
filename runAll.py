#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pytest
import os
#author:maxiunan

if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir','./report/xml'])
    os.system("allure generate ./report/xml -o ./reportml/ --clean")
    # pytest.main(['s', '--alluredir', './report/xml'])