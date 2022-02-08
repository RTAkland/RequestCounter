import sqlite3

conn = sqlite3.connect('../assets/theme.db')
cursor = conn.cursor()
cursor.execute('select * from sqlite_master where type="table"')
data = cursor.fetchall()
print(data)
