import MySQLdb
import MySQLdb.cursors

conn = MySQLdb.Connect (
host = 'localhost', user = 'root' ,
passwd = '123456', db = 'python', compress = 1,
cursorclass = MySQLdb.cursors.DictCursor, charset='utf8') 

cursor = conn.cursor()
cursor.execute ("SELECT name, txt FROM test")
rows = cursor.fetchall()
cursor.close()
conn.close()

for row in rows:
	print row ['name'], row ['txt'] # bingo!
 

# another (even better) way is:

conn = MySQLdb . Connect (
host = ' localhost ', user = 'root' ,
passwd = '', db = 'test' , compress = 1)
cursor = conn.cursor (cursorclass = MySQLdb.cursors.DictCursor)
# ...
# results by field name
cursor = conn.cursor()
# ...
# ...results by field number
