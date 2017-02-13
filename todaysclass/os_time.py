import os
import time
#check file attirbutes..

a=os.stat('log.txt')

d=time.time() - a.st_mtime
print d

if d/60 > 10:
	shutil.remove('log.txt')


