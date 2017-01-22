#Starting of modules...
import os

#You can create a directory..
#You can remove a directory.
#you can copy, move files/directories
#You can execute system commands/os commands
#file/directory exists or not u can find...

#Creating a directory...
#1: if folder already exists, delte it and then create..
#2 if folder already exists, just print folder already crated 

#second method
if os.path.exists(r"pythonosdemo"):
	print "Folder already created and now no need to create again..."
else:
	os.mkdir("pythonosdemo")


#first method..
if os.path.exists(r"c:\madhav"):
	print "folder already there, and i will delete it.."
	os.rmdir("madhav")
os.mkdir("madhav")

