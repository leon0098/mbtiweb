'''
Created on Jun 12, 2014

@author: xiafeng
'''
import types


def createSql(tableName, fieldNames, fieldValues):
    delimiter = ','
    fieldSql = delimiter.join(fieldNames)
    valueSql = listToSqlString(fieldValues)
    sql = "insert into " + tableName + " (" + fieldSql + ") values (" + valueSql + ");"
    return sql
    
    
def listToSqlString(list):
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
