import csv

#CSV file reading in python..
f = open('demo_file.csv',"r")

file_content = csv.reader(f) #it will read csv file contents..

for i in file_content:
	print i


	
'''
#logic for printing salaries grater than 15k
c=0
for i in file_content:
	if c > 0:
		if int(i[-1]) > 15000:
			print i[-1]
	c=c+1
'''


f_write = open('demo_emp.csv',"w")
write_content = csv.writer(f_write)
for i in file_content:
  del i[1]
  write_content.writerow(i)
