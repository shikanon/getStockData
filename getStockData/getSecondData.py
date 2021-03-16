#coding:utf-8
import os
import tushare as ts

all_stock_info = ts.get_stock_basics()

def CheckDirExist(rootPath):
    '''
    检查目录是否存在,并创建子目录
    '''
    if not os.path.exists(rootPath):
        os.mkdir(rootPath)

    for s in all_stock_info.index:
        child = rootPath + "/" + s
        if not os.path.exists(child):
            os.mkdir(child)
