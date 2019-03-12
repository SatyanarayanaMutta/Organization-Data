import sqlite3,cgi,time
print("Content-Type:text/html\r\n\r\n")
#size=0
#time1=Null

conn=sqlite3.connect("mydb")
cur=conn.cursor()
form=cgi.FieldStorage()
rno=form.getvalue("rno")
name=form.getvalue("name")
mobile=form.getvalue("mobile")

print('''<body bgcolor=#78dfwe><center><h1 style="font-size:40pt; background-color: DodgerBlue; color:Green">Summery Of Registration<h1><b/><h1/></center>
	<center>
	
	<table title="Data Summery" border=5 border color="7846512" style='border-color:blue'>
	<tr>
	 <td>Entered Data</td>
	 <td>
	''',rno,name,mobile)
sql="insert into employees values('"+rno+"','"+name+"',"+mobile+");"
sql1="insert into Details values('"+rno+"','"+name+"',"+mobile+");"
print("</td></tr><tr><td>Excuted SQL Command</td><td>",sql,"</td></tr>")
size=(len(rno)+len(name)+len(mobile))
print("<tr><td>Length of Data</td><td>",size,"</td></tr>")
try:
	rs=cur.execute(sql)
	rs1=cur.execute(sql1)
except Exception as e:
	print("<tr bgcolor='red'><td >Exception</td><td> ")
	print(e,"</td></tr></table><br/>")
	print('''
		<a href='../insert.html'><input type='button' value='ANOTHER REGISTER'></a>
		<a href='../edit.html'><input type='button' value='UPDATE DATA'></a>
		<input type="submit" value="SHOW" onclick="location.href='/cgi-bin/read.py'">
		<a href='../delete.html'><input type='button' value='UNREGISTER'></A>
	

	</center>
	<br/><center><a href='../index.html'><input type="submit" value="HOME" ></a></center>		''')
	
else:
	conn.commit()
	time1=time.ctime()
	print("<tr><td>Insertion Time</td><td>",time1,"</td></tr>")
	print("<tr><td>RESULT</td><td>succesfully inserted</td></tr></table><br/>")

	print('''
		<a href='../insert.html'><input type='button' value='ANOTHER REGISTER''></a>
		<a href='../edit.html'>
		<input type="submit" value="UPDATE DATA" onclick="location.href='edit.html'"></a>
	<input type="submit" value="SHOW" onclick="location.href='/cgi-bin/read.py'">
	<a href="..\delete.html"><input type="button" value="Remove"></a>

	</center>
	<br/><center><input type="submit" value="HOME" onclick="../index.html"></center>		''')
finally:
	conn.close()
	cur.close()
	