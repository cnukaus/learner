import unittest

class testcase(unittest.TestCase):
	def test1(self):
		self.assertEqual(sum([1,1]),3,"Equal")
	def test2(self):
		self.assertEqual("1"+"2","12","samestring")
if __name__== '__main__':
	unittest.main()