#import os
#import pathlib
#from pathlib import Path
# def current_directory():
#     cwd=os.getcwd()
#     print("current working directory is: ",cwd)

# current_directory()
# def file_path(filename):
#     path=os.path.abspath((filename))
#     print(path)

# filename="sample.txt"
# file_path(filename)

#os.path.abspath("sample.txt")
#print(Path.cwd())

#print(pathlib.Path().absolute())

#print(os.path.abspath('sample.txt'))

#pythonfile = 'sample.txt'

# if the file is present in current directory,
# then no need to specify the whole location
#print("Path of the file..", os.path.abspath(pythonfile))

# for root, dirs, files in os.walk(r'C:\python36'):
# 	for name in files:
	
# 		# As we need to get the provided python file,
# 		# comparing here like this
# 		if name == pythonfile:
# 			print(os.path.abspath(os.path.join(root, name)))

#import time
#print(time.time())
#rty=time.time()
#print(rty)
#localtime=time.localtime(rty)
#print(localtime.tm_year)
#print(time.ctime(rty))

#SMTP Module
#sending mail

# import smtplib

# smtpobj=smtplib.SMTP('smtp.gmail.com', 587)
# smtpobj.ehlo()
# smtpobj.starttls()
# smtpobj.login("pusparghyamukherjee10@gmail.com",'ARYANREDONTIGER45610')


