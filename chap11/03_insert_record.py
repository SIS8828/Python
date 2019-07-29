import sqlite3

sql = """
insert into phonebook values(?,?,?)
"""

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute(sql,('홍길동','1111-1111-111','islu@ilsu.il'))

id = cursor.lastrowid
print(id)

cursor.execute(sql,('강감찬','010-4444-4444','kang@ilsu.il'))

id = cursor.lastrowid
print(id)

conn.commit()

cursor.close()
conn.close()