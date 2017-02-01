#tuples
#string(immtable) vs list(mutable)
#list(mutable) vs tuples(immutable)

#tuple determnation it is hashed array..
#list is not hashed array..

a=[1,2,3,4,5]
print type(a)

a[3]=89
print a
a=tuple(a)
print type(a)
print a

#a[3]=90

