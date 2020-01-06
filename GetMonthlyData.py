import mysql.connector
import sys
import csv
from datetime import datetime
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

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
        datestring=str(row[0])+"-"+str(row[1])
        string = datetime.datetime.strptime(datestring, '%Y-%m')
        data= (string, row[2]/30, row[3]/30)
        if result[0] == row:
            data_list.append(["Datetime","Humidity","Temparature"])
        data_list.append(data)

#print(data_list)

##################### Testing Program End

fp = open('monthly-weather-report.csv', 'w') ##different path but you get the idea
myFile = csv.writer(fp, lineterminator='\n')
myFile.writerows(data_list)
fp.close()

#print(result)   # (datetime.datetime(2007, 5, 9, 4, 0), 6.38, 0.52, 74.41)

#print(result[0][0]) # "2007-05-09 04:00:00"

df = pd.DataFrame(pd.read_csv('monthly-weather-report.csv'))
df['Datetime'] = pd.to_datetime(df['Datetime'])
df.head()
#df.plot.bar()
#fig, ax = plt.subplots(figsize=(10, 10))
#ax.plot(['Datetime',''], ['Humidity', 'Temparature'])
#ax.plot(df['Datetime'],[df['Humidity'],df['Temparature']])
#ax.set(xlabel="Date&Month", ylabel="Humidity", title="Characterstics of Humidity")

df.plot(x="Datetime",y=["Humidity","Temparature"], marker='o', linestyle='-', grid=True, title="Characterstics of Humidity & Temparature")
plt.xlabel("Date&Time")
plt.ylabel("Humidity & temparature")

plt.show()

