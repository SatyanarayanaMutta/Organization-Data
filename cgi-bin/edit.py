import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("mydb")
cur=conn.cursor()
#record=""
form=cgi.FieldStorage()
rno=form.getvalue("rno")
query="select * from employees where rno="+rno
print('''<style type="text/css">
		input[type=text]{height: 30px;font-size: 18px;}
		input[type=number]{height: 30px;font-size: 18px;}
	</style>
	<center>
	<h1 style="font-size:30pt; background-color: DodgerBlue; color:Green"><u><b>Employee Data Updation</b></u><h1/>
		</center>
		<br><br>''')

try:
	cur.execute(query)
	print(cur)
except Exception as e:
	print(e)
	#print('''<body>no data</body></html>''')
else:
	for record in cur:
		pass
	html='''<html><head><title>Updation of Data</title></head><body bgcolor=#78zdwa>
	<form action="update.py" method="PUT">
	<table align="center" style='border-color:blue'><tr><td>
	<input type="text" value="%d" name="rno" class="field left" readonly>
	<td/><tr/><tr><td>
	<input type="text" value="%s" name="name">
	<td/>
	<tr/><tr><td>
	<input type="number" value="%s" name="mobile"><br/>
	<td/><tr/></table>
	<center>
	<input type="submit" value="Update" >
	</form>  &emsp;
	<a href='../edit.html'><input type='button' value='CANCEL'></a>
	</center><br/><center>
	<a href='../index.html'><input type='button' value='HOME'></a>
	</center>
	</body>
	</html>'''%(record[0],record[1],record[2])
	print(html)

	"""else:
		print('''<body>
			No Data
		</body>
			''')"""
finally:
	cur.close()
	conn.close()
	
