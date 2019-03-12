import sqlite3,cgi,time
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("mydb")
cur=conn.cursor()
form=cgi.FieldStorage()
rno=form.getvalue("rno")
name=form.getvalue("name")
mobile=form.getvalue("mobile")
print('''<center><h1 style="font-size:40pt; background-color: DodgerBlue; color:Green">Summery Of Updation</h1></b></h1></center>''')
print("<body bgcolor='red'><table align='center' bgcolor='lightgreen' border=5 style='border-color:blue'><tr><td>Entered Data</td>")
print("<td>",rno,name,mobile,"</td></tr><tr><td>SQL Query</td><td>")
sql="update employees SET name='"+name+"' ,mobile="+mobile+" where rno="+rno
print(sql,"</td></tr>")
size=(len(rno)+len(name)+len(mobile))
print("<tr><td>Length of Data</td><td>",size,"</td></tr>")
try:
	rs=cur.execute(sql)

	
except Exception as e:
	print("<tr bgcolor='red'><td >Exception</td><td> ")
	print(e,"</td></tr><tr><td align='center'><a href='../insert.html'><input type='button' value='Back' style='width:100px;'></a></td><td align='center'><a href='../edit.html'><input type='button' value='Edit' style='width:100px;'></a></td></table>")
	
else:
	conn.commit()
	time1=time.ctime()
	print("<tr><td>Insertion Time</td><td>",time1,"</td></tr>")
	print("<tr><td>RESULT</td><td>succesfully inserted</td></tr></table><br/>")
	print('''<center>
		<a href='../insert.html'><input type='button' value='REGISTER'></a>
		<a href='../edit.html'><input type='button' value='UPDATE DATA'></a>
		<input type="submit" value="SHOW" onclick="location.href='/cgi-bin/read.py'">
		<a href='../delete.html'><input type='button' value='UNREGISTER'></A>
		</center><br/>
		<center><a href='../index.html'><input type="submit" value="HOME" ></a></center>''')
finally:
	conn.close()
	cur.close()