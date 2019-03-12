import sqlite3,cgi,time
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydb")
cur=conn.cursor()
form=cgi.FieldStorage()
rno=form.getvalue("rno")
print('''<body bgcolor="#24fd47"><center><h1 style="font-size:40pt; background-color: DodgerBlue; color:Green">Summery Of Registration<h1><b/><h1/></center>
	<center>
	
	<table title="Data Summery" border=5 bgcolor="#f8457z" style='border-color:blue'>
	<tr>
	 <td>Entered Data</td>
	 <td>
	''',rno)
query="delete from employees where rno="+rno
print("</td></tr><tr><td>Excuted SQL Command</td><td>",query,"</td></tr>")
#size=(len(rno)
#print("<tr><td>Length of Data</td><td>",size,"</td></tr>")
try:
	cur.execute(query)
except Exception as e:
	print("<tr bgcolor='red'><td >Exception</td><td> ")
	print(e,"""</td></tr></table>
		<br/><center><a href='../insert.html'><input type='button' value='Back' style='width:100px;'></a>
		<a href='../edit.html'><input type='button' value='Edit' style='width:100px;'></a></center><br/>
		<center><a href='../index.html'><input type='button' value='HOME' style='width:100px;'></a></center>""")
	
else:
	conn.commit()
	time1=time.ctime()
	print("<tr><td>Insertion Time</td><td>",time1,"</td></tr>")
	print("<tr><td>RESULT</td><td>Deleted succesfully</td></tr></table>")
	print('''<br/>
		<center>
		<a href='../insert.html'><input type='button' value='REGISTER'></a>
		<a href='../edit.html'><input type='button' value='UPDATE'></a>
		<a href='read.py'><input type='button' value='SHOW'></a>
		<a href='../delete.html'><input type='button' value='DELETE'></a>
		</center><br/>
		<center>
		<a href='../index.html'><input type='button' value='HOME'></a>
		</center>''')
finally:
	conn.close()
	cur.close()
	