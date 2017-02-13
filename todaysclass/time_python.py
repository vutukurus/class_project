#os module
import time

print time.time() #time in seconds.

a = time.localtime(time.time())
print a
print str(a.tm_year)+'-'+str(a.tm_mon)

print time.asctime(time.localtime(time.time()))


#sleep..

print "before sleep"
time.sleep(5) #seconds..
print "after sleep"
