'''
Created on Jun 11, 2014

@author: xiafeng
'''
import xlrd

data = xlrd.open_workbook('data.xlsx')

table = data.sheet_by_name("Sheet1")

nrows = table.nrows

nclos = table.ncols

for i in range(nrows):
    print table.row_values(i)

    