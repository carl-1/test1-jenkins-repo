import os
import stat

try:
	file = open("hello.txt")
except IOError:
	print ("Encountered an error in file IO operations, File not found...creating it")
	file = open("hello-excep.txt", "w+")
	file.write("hello-excep........")
#except NextExceptionHere:
	
else:#the default block
	print ("No IO error detected")
	print ("Opening the file %s for writing" %file.name)
	file_1 = open("hello.txt", "w")
	# starting from RHS - others_access/group_access/owner
	#os.chmod(file.name, stat.S_IWOTH | stat.S_IWGRP | stat.S_IWUSR | stat.S_IWRITE) # changing permission of the file
	#os.chmod(file.name, 0000)
	file_1.write("hello..hello...hello..sending new data")
finally:
	file.close()
	file_1.close()
print ("File opened is : %s by Mr. %s " %(file.name, "Carl"))	