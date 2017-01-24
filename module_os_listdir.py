import os #importing a module..
import sys
import shutil

#get source directory from user..
#raw_input
src_dir = raw_input("Please enter source directory path:")

if os.path.exists(src_dir):
	print "Source dir is valid and contining for next steps"
else:
	print "You gave wrong path..please check.."
	sys.exit(1) #used to comeout of the script from any point...

#print src_dir

dest_dir = raw_input("Please enter destination directory path:")

if os.path.exists(dest_dir):
	print "destination dir is valid and contining for next steps"
else:
	print "You gave wrong path..please check.."
	sys.exit(1) #used to comeout of the script from any point...


filter = raw_input("Which extension files to copy:")

get_files_list = os.listdir(src_dir)

for i in get_files_list:
	if i.endswith('.'+filter):
		print i
		shutil.copy(src_dir+"\\"+i,dest_dir+"\\"+i)
