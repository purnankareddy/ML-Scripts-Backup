import mysql.connector
import sys
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

QUERY="""SELECT datetime, windspeed, humidity, temparature FROM weatherdata WHERE datetime < '2008-04-01 04:00:00' AND datetime > '2007-05-01 04:00:00'"""
mycursor.execute(QUERY)
result=mycursor.fetchall()

################### Testing Program start
#print(mycursor.rowcount)
data_list = []

if not mycursor.rowcount:
    print('Error #4')
    print('No Log on this date found')
else:
#    print('printed')
    for row in result:
        data= (row[0], row[1], row[2], row[3])
        data_list.append(data)

#print(data_list)

##################### Testing Program End

fp = open('datafile.csv', 'w') ##different path but you get the idea
myFile = csv.writer(fp, lineterminator='\n')
myFile.writerows(result)
fp.close()

#print(result)   # (datetime.datetime(2007, 5, 9, 4, 0), 6.38, 0.52, 74.41)

#print(result[0][0]) # "2007-05-09 04:00:00"

