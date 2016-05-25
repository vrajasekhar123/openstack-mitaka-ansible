#!/usr/bin/python
import MySQLdb
import sys
password=sys.argv[1]
try:
   db=MySQLdb.connect("localhost","root")
except:
   db=MySQLdb.connect("localhost","root",password,"mysql")
cursor = db.cursor()
sql="GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY '"+password+"';"
sql1="GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '"+password+"';"
cursor.execute(sql)
cursor.execute(sql1)
cursor.close()
db.close()
