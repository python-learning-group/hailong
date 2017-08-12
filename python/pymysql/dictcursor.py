#!/usr/bin/python3

import pymysql

db = pymysql.connect('127.0.0.1','root','handhand','test')

cur = pymysql.cursors.DictCursor(db)

