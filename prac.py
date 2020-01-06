# Python program to find current 
from datetime import datetime
import time
import requests, json

# Python mysql DB connect lines
import mysql.connector
import random
from datetime import datetime
from sample import tb 

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password",
  database="mydatabase"
)
latitude="13.030087"
longitude="77.657284"
datetimes=tb()

mycursor = mydb.cursor()

# Enter your API key here 
#api_key = '96df4121f48572f1743ad4a782a0713e'
#api_key = 'bb1ceced30d040834df3dd7e645b7cac'
#api_key= 'd8a69f0567afcca15fe0ed09366f0556'
#api_key= 'f629365a1f04f6bdb2ea7dad3fe3a1a1'
#api_key='a530b3ed864a25caa0b496f47e936913'
#api_key='48ce42e8afea06592ebf24c080b5767b'
#api_key='626ebe9e2a22536297655f0612d8dbd0'
api_key='3b81ba46090832322ef1670282ca328b'

# base_url variable to store url 
base_url = "https://api.darksky.net/forecast/"
for dtime in datetimes:
    # complete url address 
    complete_url = base_url + api_key + "/" + latitude +","+ longitude +","+ str(dtime) + "?" + "exclude=currently,flags"
    print(complete_url)
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    # json method of response object 
    time.sleep(0.5)
    x = response.json() 

    city_name=x["timezone"]
    current_humidity=x["hourly"]["data"][0]["humidity"]
    weather_description="Bangalore data not available"
    #weather_description=x["daily"]["data"][0]["icon"]
    wind_speed=x["hourly"]["data"][0]["windSpeed"]

    ts=int(x["hourly"]["data"][0]["time"])
    responsedtime=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    temp_high = x["hourly"]["data"][0]["temperature"]
    #temp_low = x["daily"]["data"][0]["temperatureLow"] 

    #current_temperature = (temp_high+temp_low)/2
    current_temperature = temp_high

    print("City Name: "+city_name+" Date&Time: "+responsedtime+" Wind-speed: "+str(wind_speed)+" humidity: "+str(current_humidity)+" weather_discription: "+str(weather_description)+" current_temperature:"+str(current_temperature))
    sql = """INSERT INTO weatherdata (cityname, datetime, windspeed, humidity, temparature, discription) VALUES (%s,%s,%s,%s,%s,%s)"""
    val = (city_name, responsedtime, str(wind_speed), str(current_humidity), str(current_temperature), str(weather_description))
    mycursor.execute(sql,val);
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    time.sleep(0.5)
    
    if responsedtime == "2002-06-29 05:00:00" :
        print("date%time to breake is : "+responsedtime)
        break;

#    a = input("Enter yes/no to continue")
#    if a=="yes":
#        continue
#    elif a=="no":
#        break


