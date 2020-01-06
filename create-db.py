import mysql.connector

mydb = mysql.connector.connect(
  #host="192.168.1.4",
  host="localhost",
  user="purna",
  passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
