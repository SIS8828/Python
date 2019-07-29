import sqlite3

sql ="delete from phonebook where email = ?"

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute(sql,('islu@ilsu.il',))

conn.commit()

cursor.execute("select * from phonebook")
rows = cursor.fetchall()

for row in rows:
    print("name:{0}, phone:{1},email:{2}".format(row[0],row[1],row[2]))

cursor.close()
conn.close()
