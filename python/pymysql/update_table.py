#!/usr/bin/python3

import pymysql

db = pymysql.connect('127.0.0.1','root','handhand','test')

cur = db.cursor()

sql = "update employee set age = age + 1 where sex = '%c'"%('M')

try:
    cur.execute(sql)
    db.commit()

except:
    db.rollback()

db.close()