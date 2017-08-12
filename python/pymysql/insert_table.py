#!/usr/bin/python3

import pymysql

db = pymysql.connect('127.0.0.1','root','handhand','test')

cur = db.cursor()

sql = """
    insert into employee(
        first_name,last_name,age,sex,income
    ) values(
        'mac','mohan',20,'M',2000
    )
"""

sql1 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()