import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO `weather` (`sno`, `city-name`, `temp`, `pressure`, `humidity`, `desc`) VALUES (NULL, city_name, str(current_temperature), str(current_pressure), str(current_humidiy), str(weather_description))")

