'''
Created on Jun 12, 2014

@author: xiafeng
'''
import types


def createSql(tableName, fieldNames, fieldValues):
    delimiter = ','
    fieldSql = delimiter.join(fieldNames)
    valueSql = listToString(fieldValues)
    sql = "insert into " + tableName + " (" + fieldSql + ") values (" + valueSql + ");"
    return sql

# fieldNames = [u'id', u'name', u'description']
# fieldValues = [1.0, u'p1', u'\u6d4b\u8bd51']
# createSql("paper",fieldNames, fieldValues)
    
def listToString(list):
    listStr = ""
    for i in range(len(list)):
        value = list[i]
        valueType = type(value)
        if valueType is types.StringType or valueType is types.UnicodeType:
            value = "'" + value + "'"
            listStr = listStr + value + ","
        elif valueType is types.FloatType:
            listStr = listStr + str(value) + ","
    return listStr[:-1]
 
# delimiter = ','
# mylist = ['Brazil', "b", 'India', 'China']
# print delimiter.join(mylist)

# list = [1.0, u'p1', u'\u6d4b\u8bd51']
# print listToString(list)

# print str(1.0)+"abc"

# tableName = "paper_paper"
# fieldNames = [u'id', u'name', u'description']
# fieldValues = [1.0, u'p1', u'\u6d4b\u8bd51']
# print createSql(tableName, fieldNames, fieldValues)
