#Python Debbuging..
import pdb

a=[1,2,3,4,5,6]

for i in a:
	i=i+9
	pdb.set_trace()
	i=i+90
	print "i value after i is %s" %i