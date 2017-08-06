#!/usr/bin/env python
# coding=utf-8

import sys
import os

# sys.argv 命令行参数
print('the file name:', sys.argv[0])
print('the number of argument', len(sys.argv))
print('the argument is:', str(sys.argv))

#sys.exit() 推出程序 类似 return


# os
# os.rename('oldvalue','newvalue')
# os.rename("22201.py", "newtemp.py")

# os.remove('file') 移除文件
# os.remove("/home/qw/Documents/VBS/StarterLearningPython/2code/rd/a.py") 

# os.listdir 显示目录中的内容（包括文件和子目录）。
# os.listdir("/home/qw/Documents/VBS/StarterLearningPython/2code/rd")
# os.getcwd：当前工作目录；os.chdir：改变当前工作目录
# os.chdir("rd")         #进入下级  os.pardir的功能是获得父级目录
# os.makedirs, os.removedirs：创建和删除目录

# os.stat() 文件和目录属性

p = os.getcwd()
print(p)
command = 'ls ' + p
os.system(command)

#>>> import webbrowser 在浏览器打开链接，http不能省
# webbrowser.open("http://www.itdiffer.com")