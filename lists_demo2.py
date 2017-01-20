#append, insert, del, remove, pop
#index, count, sort,reverse
#i am adding one more change here...


a=[10,20,30,50]
#how to change/modify list elements
a[2]=90
print a

print a[0:2]
a[0:2]=[89,87]
print a

#How to append/add elemnts to a list...
#append method.
a.append(1000)
a.append(2000)
print a

#insert method: This is mainly used for adding or inserting elements at user desired index...
#a.insert(index, value)
a.insert(1,56)
a.insert(5,"perl")
print a

#deleting elements in list..
del a[2]
print a

#remove 
a.remove(89)
print a

#pop.
a.pop()
print a

