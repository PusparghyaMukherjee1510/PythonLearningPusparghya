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


#create file in folder
# import os
# from os import path

# def create_file(dest):
#     if not(path.isfile(dest)):
#         f=open(dest,'w')
#         f.write("Updating Python")
#         f.close()
# test="C:\\Users\\USER\\Desktop\\TxTs\\pample.txt"
# create_file(test)

# print("File Created Once Again")

#sending mail

# import smtplib

# smtpojj=smtplib.SMTP('smtp.gmail.com', 587)
# smtpojj.ehlo()
# smtpojj.starttls()
# smtpojj.login('pusparghyamukherjee10@gmail.com','ARYANREDONTIGER45610')
# smtpojj.sendmail('pusparghyamukherjee1994@gmail.com','pusparghyamukherjee10@gmail.com', 'Subject: SMTP check from Python \n Test mail send using Python')
# smtpojj.quit()

# def funcl(*args):
#     for i in args:
#         print(i)

# funcl(1,3,5,6,'ghjk',8.96)

# def fubn(*args,**kwargs):
#     for i in kwargs.items():
#         print(i)

# fubn(a=10,b=89,c=53)

# def func1():
#     x=10
#     def func2(x):
#         return x+1
#     return func2(x)

# print(func1())

#create class during runtime
# B=type("BaseClass",(object,),{})
# C1=type("C1",(B,),{'val':50})
# C2=type("C2",(B,),{'val':100})

# def classCreator(bool):
#     if bool:
#        return C1()
#     else:
#         return C2()

# print(classCreator((True).val))
# print(classCreator((False).val))
