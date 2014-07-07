'''
Created on Jul 7, 2014

@author: xiafeng
'''
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='mbti_mysql_passw0rd', db='test', port=3306)
    cur = conn.cursor()
    cur.execute('select * from user')
    cur.close()
    conn.close()
except MySQLdb.Error, e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
