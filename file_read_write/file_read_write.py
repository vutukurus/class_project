#git.txt read...
#readed data u will save to other file..

#read git.txt
file_handle=open(r"C:\Users\siv\Desktop\git.txt","r")
#rude way, read, readlines

read_list = file_handle.readlines()


file_handle.close()

#write to another file or paste to another file..

write_handle = open(r"C:\Users\siv\Desktop\git_copied.txt","w")

for i in read_list:
	if i.find("command") >= 0: # Filter condition..
		write_handle.write(i)

write_handle.close()