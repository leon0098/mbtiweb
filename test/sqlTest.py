'''
Created on Jun 12, 2014

@author: xiafeng
'''
import sqlite3
cx = sqlite3.connect("test.db")

# con.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")
# 
# for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
#     con.execute("insert into catalog values (?,?,?,?)", t)
#     
# con.commit() 

cu=cx.cursor() 
cu.execute("select * from catalog")  
list = cu.fetchall()  
print list