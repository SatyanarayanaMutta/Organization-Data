import sqlite3
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydb")
cur=conn.cursor()
query="select * from employees"
html='''
<html>
<head><title>Employees Data</title></head>
<body bgcolor="#9612cv"><center><h1 style="font-size:40pt; background-color: DodgerBlue; color:Green">EMPLOYEES DATA<h1><b/><h1/></center>
	<center>
<table border=2 style='border-color:blue' align="center">
<tr><td></td><td align="center">EMPLOYEES DATA</td></tr><tr><td>RIGISTER ID</td><td>EMPLOYEE NAME</td><td>MOBILE NUMBER</td></tr>
'''
print(html)
try:
	rs=cur.execute(query)
except Exception as e:
	print(e)
else:
	for record in cur:
		print("<tr>")
		for column in record:
			print("<td>"+str(column)+"</td>")
		print("</tr>")
	html='''
	</table><br/>
	<center>
		<a href='../insert.html'><input type='button' value='REGISTER'></a>
		<a href='../edit.html'><input type='button' value='UPDATE'></a>
		<a href='read.py'><input type='button' value='REFRESH'></a>
		<a href='../delete.html'><input type='button' value='DELETE'></a>
		</center><br/>
		<center>
		<a href='../index.html'><input type='button' value='HOME'></a>
		</center>

</body>
</html>
	'''
	print(html)
finally:
	conn.close()
	cur.close()