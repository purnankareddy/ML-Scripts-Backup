import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE weather")
