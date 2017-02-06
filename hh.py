import os
import sys

#os commands or command line commands
#write in terms of functions..
#git add <filename>
#git commit -m "message"
#git push https://github.com/vutukurus/class_project.git

#os.system("git clone https://github.com/vutukurus/class_project.git")
#subprocess...


def add_file(filename):
	print "Invoking git add"
	os.system("git add %s" %filename)

def commit(msg):
	print "commiting hte change now.."
	os.system("git commit -m %s" %msg)

def push(repopath):
	print "Pushing hte changes, please be patience,,"
	os.system("git push %s" %repopath)

add_file(sys.argv[1])
commit(str(sys.argv[2]))
push(sys.argv[3])

