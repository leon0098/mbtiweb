# encoding: utf-8

'''
Created on Jun 11, 2014

@author: xiafeng
'''
#批量执行sql脚本    
import sqlite3


f = file('clean.sql')
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