import mysql.connector
import sys
import csv

import pandas as pd
import datetime
import numpy as np

import matplotlib.pyplot as plt
#import seaborn as sns

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password",
  database="mydatabase"
)

mycursor=mydb.cursor()

QUERY="""SELECT YEAR(datetime) as YY, MONTH(datetime) as MM, SUM(humidity) as humidity, SUM(temparature) as temparature FROM weatherdata GROUP BY MONTH(datetime), YEAR(datetime) ORDER BY YEAR(datetime), MONTH(datetime) ASC"""

mycursor.execute(QUERY)
result=mycursor.fetchall()

################### Testing Program start
#print(mycursor.rowcount)
data_list = []

if not mycursor.rowcount:
    print('Error #4')
    print('No Log on this date found')
else:
    for row in result:
        string=str(row[0])+"-"+str(row[1])
        data= (string, row[2]/30, row[3]/30)
        data_list.append(data)

#print(data_list)

##################### Testing Program End

fp = open('monthly-weather-report.csv', 'w') ##different path but you get the idea
myFile = csv.writer(fp, lineterminator='\n')
myFile.writerows(data_list)
fp.close()

#print(result)   # (datetime.datetime(2007, 5, 9, 4, 0), 6.38, 0.52, 74.41)

#print(result[0][0]) # "2007-05-09 04:00:00"

df = pd.read_csv('monthly-weather-response.csv')
df.head()
df.plot.bar()
plt.xlabel("Date&Time")
plt.ylabel("Humidity & temparature & Windspeed")


#df.set_index('Date&Time').groupby('Temparature')['Himidity'].plot(legend=True)



plt.show()


