# encoding: utf-8
'''
Created on Jun 11, 2014

@author: xiafeng
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # @UndefinedVariable

import xlrd

from common.sql import createSql


data = xlrd.open_workbook('data.xlsx')

'''
table = data.sheet_by_name("Sheet1")

nrows = table.nrows

nclos = table.ncols

for i in range(nrows):
    print table.row_values(i)
'''

#获得所有sheet名称
sheetNames = data.sheet_names()
# print sheetNames

#遍历所有sheet
for i in range(len(sheetNames)):
    tableName = sheetNames[i]
    print "sheetName:" + tableName
    table = data.sheet_by_name(sheetNames[0])
    #取第一行的表字段名
    fields = table.row_values(0)
    print "fields:" + str(fields)
    #取得sheet行数
    nrows = table.nrows
    print "nrows:" + str(nrows)
    #取每一行数据生成对应的create sql语句
    f = file("create.sql","w")
    for j in range(nrows-1):
        print "---------------------"
        values = table.row_values(j+1)
        sql = createSql(tableName,fields,values)
        f.write(sql+"\n")
        print sql
    f.close        

    