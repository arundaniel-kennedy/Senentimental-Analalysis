import pymysql

db = pymysql.connect(host='localhost:3306',user='root',passwd='root')
cursor = db.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)
for r in cursor:
print r
