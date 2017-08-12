#!/usr/bin/python3

import pymysql

db = pymysql.connect('127.0.0.1','root','handhand','test')

cur = db.cursor()

sql = "select * from employee where income>'%d'" %(1000)

try:
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print(row)
        print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
    print('error: unable to fetch data')

db.close()