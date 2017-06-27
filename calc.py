#!/usr/bin/python
import os

def mul(n1, n2):
	total = n1 * n2
	return total

nav = input("Hello...what is you name?")
#name = eval(raw_input("Enter your name: "))
#print ("You entered: ",name)
print ("Nav entered is : ",nav)
#, " the list of imported modules here are : ",dir())
filelist = os.listdir("E:\\")
print (filelist)
file1 = open("E:\\IBM\\TExT - ML\\app.log","r")#"a")
#file1.write("Carl...writing something from the Python file..")
values = file1.read(100)
#print ("entire file contents : ", file1.read())
print ("Current file position :", file1.tell()) # this gives 101 as we have already read 100 letters
# Read the next 100
position = file1.seek(10,0) # from 0 to 100, move (remove?)
next = file1.read()
print ("Seeked position read is : ",next)
file1.close()
print ("Data read is : ",values)
#rename the file
os.rename("E:\\IBM\\TExT - ML\\app.log", "E:\\IBM\\TExT - ML\\app123.log")
print ("File name has been renamed to : ",file1.name)#renamed file's name not reflecting here, same old one showed
os.rename("E:\\IBM\\TExT - ML\\app123.log", "E:\\IBM\\TExT - ML\\app.log")
# os.remove(file_name) - delete a file
# os.mkdir("newdir") - make a new dir
# os.chdir("newdir") - change to dir
# os.getcwd() - get current working dir
# os.rmdir('dirname') - delete dir
# print "Name of the file: ", fo.name print "Closed or not : ", fo.closed print "Opening mode : ", fo.mode