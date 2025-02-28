#!C:\Program Files\Python313.exe
import cgi
import mysql.connector


print("Content-Type: text/html\n\n")
print("<html>")
print("<body>")
print("<h1>Thank You for ordering</h1>")


form=cgi.fieldstorage()
name=form.getvalue("name")
product=form.getvalue("product")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="orderform"
)
mycursor=mydb.cursor()
sql="INSERT INTO details(name,product) values(%s,%s)"
val=(name,product)
mycursor.execute(sql,val)
mydb.commit()

print("<h1>",name,product,"</h1>")

print("</body>")
print("</html>")