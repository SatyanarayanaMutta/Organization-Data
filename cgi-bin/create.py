import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydb")
cur=conn.cursor()
query="create table employees(rno varchar,name varchar,mobile number)"
try:
	cur.execute(query)
except Exception as e:
	print(e)
else:
	conn.commit()
	print("created successfully")
finally:
	conn.close()
	cur.close()
