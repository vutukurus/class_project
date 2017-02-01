#File operations

#3 modes of operations.
#read --> reading the content in a file(r)
#write --> writing data to a file(w)
#append  --> appends data to end of a file(a)

file_handle = open(r"C:\Users\siv\Desktop\git.txt", "r")


#read vs readlines..
#print file_handle.read()
d=file_handle.readlines()
for i in d:
	if i.find("ex:") >= 0:
		print i



"""
#rude way:
for i in file_handle:
    if i.find("command") >= 0:
		print i
"""
#Mandatory u should close..
file_handle.close()