#!C:\Program Files\Python.exe
import cgi
import mysql.connector

print("Content-type: text/html/n/n")
print("<html>")
print("<body>")
print("<h1>"Thank You for ordering"</h1>")

form=cgi.Fieldstorage()
name=form.getvalue("Name")
product=form.getvalue("Product")

print("<h1>Name,Product,</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="orderform"
)
mycursor=mydb.cursor()
datas=(name,product)
sql="INSERT INTO orderdetails (Name,Product) values(%s,%s)"
mycursor.execute(sql,datas)
mydb.commit()
print("</body>")
print("</html>")
