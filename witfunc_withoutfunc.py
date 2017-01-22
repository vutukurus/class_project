a=[1,5,3,4,3,5,3]

#With function..
def find_index(number):
	c=0
	for i in a:
		
		if i == number:
		   print "This value belongs to number %s and its index is %s" %(number,c)
		c = c+1

find_index(3)		
find_index(5)		


#Without finctions
'''
c=0
for i in a:
    
    if i == 3:
       print c
    c=c+1
	
c=0
for i in a:
    
    if i == 5:
       print c
    c=c+1
'''