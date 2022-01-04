import requests
from bs4 import BeautifulSoup
import pyodbc
import datetime
import json
import objectpath
import time


conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=10.7.2.125;'
                         'Database=AR_B2K_CRO_UAT;'
                         'Trusted_Connection=yes;'
                          )

cursor = conn.cursor()

list = [123456, 123457]



#print(list)

t = tuple(list)

#print(t)



#query = 'select * from crmcoff where crmCOFF_RefNo in {};'.format(t)

query2 = 'select * from crmcoff where crmCOFF_RefNo in %s' % repr(tuple(map(str,list)))

cursor.execute(query2)

data = cursor.fetchall()

print(data)

#for index, tuple in enumerate(data):
#	element_one = tuple[0]
#	element_two = tuple[1]
#
#	print(element_one, element_two)


for row in data:

    column1 = row[0]
    column2 = row[1]
    column3 = row[2]


    print(column1,column2,column3)




