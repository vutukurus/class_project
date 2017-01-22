#This function is used to find len of a list.


#input- list
#output - int
def len_list(input_list):
	counter = 0
	for i in input_list:
		counter=counter+1
	return counter

#print len_list([1,2,3,3,5,6])

def test(a,b):
	return a+b