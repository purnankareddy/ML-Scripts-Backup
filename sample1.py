# Python program to find current 

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
latitude="42.3601"
longitude="-71.0589"
datetimes=tb()

#mycursor = mydb.cursor()

# Enter your API key here 
api_key = '96df4121f48572f1743ad4a782a0713e'


# base_url variable to store url 
base_url = "https://api.darksky.net/forecast/"
for datetime in datetimes:
    # complete url address 
    complete_url = base_url + api_key + "/" + latitude +","+ longitude +","+ str(datetime) + "?" + "exclude=currently,flags"
    print(complete_url)
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    # json method of response object 
    x = response.json() 

    city_name=x["timezone"]
    current_humidity=x["daily"]["data"][0]["humidity"]
    weather_description=x["daily"]["data"][0]["summary"]
    wind_speed=x["daily"]["data"][0]["windSpeed"]
    date_time=

    temp_high = x["daily"]["data"][0]["temperatureHigh"]
    temp_low = x["daily"]["data"][0]["temperatureLow"]

    current_temperature = (temp_high+temp_low)/2


    print("City Name: "+city_name+" Wind-speed: "+str(wind_speed)+" humidity: "+str(current_humidity)+" weather_discription: "+str(weather_description)+" current_temperature:"+str(current_temperature))
    a = input("Enter yes/no to continue")
    if a=="yes":
        continue
    elif a=="no":
        break

#sql = """INSERT INTO weather (sno, cityname, temp, pressure, humidity, discreption) VALUES (%s,%s,%s,%s,%s,%s)"""
#val = (random.randrange(6,10,3), city_name, str(current_temperature), str(current_pressure), str(current_humidity), str(weather_description))
#mycursor.execute(sql,val);
#mydb.commit()

#print(mycursor.rowcount, "record inserted.")


