#Unit testing..
#contunoust integration -- hudson/jenkins

import unittest

def test_fun(a):
	a=a+1
	return a


class MyTest(unittest.TestCase):
	def test(self):
		self.assertEqual(test_fun(5),6)

   
unittest.main()
