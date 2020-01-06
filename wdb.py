import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="purna",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [

  ('Temperature (in kelvin unit)', '299.55'),
  ('atmospheric pressure (in hPa unit)', '1017'),
  ('humidity (in percentage):', '65'),
  ('description:', 'scattered clouds')

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 
