'''
파이선 SQLite 연동 절차


'''

import sqlite3

# phonebook 테이블 생성
sql = """
create table phonebook(
    name char(32),
    phone char(32),
    email char(64) primary key
    )



# test.db 파일 안에 phonebook테이블 생성

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute(sql)

cursor.close()
conn.close()
"""




