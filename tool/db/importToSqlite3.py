# encoding: utf-8

'''
Created on Jun 11, 2014

@author: xiafeng
'''
import sqlite3
import sys

import xlrd

from common.sql import createSql


reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable


data = xlrd.open_workbook('data.xlsx')
# 获得所有sheet名称
sheetNames = data.sheet_names()
    
# 遍历所有sheet
f = file("create.sql", "w")
for i in range(len(sheetNames)):
    tableName = sheetNames[i]
    print "sheetName:" + tableName
    table = data.sheet_by_name(sheetNames[i])
    # 取第一行的表字段名
    fields = table.row_values(0)
    print "fields:" + str(fields)
    # 取得sheet行数
    nrows = table.nrows
    print "nrows:" + str(nrows)
    # 取每一行数据生成对应的create sql语句
    for j in range(nrows - 1):
        values = table.row_values(j + 1)
        sql = createSql("paper_"+tableName, fields, values)
        f.write(sql + "\n")
        print sql
f.close 

    
#批量执行sql脚本    
f = file('create.sql')
cx = sqlite3.connect("../../db.sqlite3")
cu = cx.cursor() 
while True:
    sql = f.readline()
    if len(sql) == 0:  # Zero length indicates EOF
        break
    print sql
    cu.execute(sql)
f.close() 
cx.commit()    

    
