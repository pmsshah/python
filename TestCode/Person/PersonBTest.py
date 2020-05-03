import unittest

class Testing(unittest.TestCase):
	def setUp(self):
		print ("Running Unit Test :", __file__);

	def tearDown(self):
		print ("Done Running Unit Test :", __file__);

        
	def test_string(self):
		a = 'some'
		b = 'some'
		self.assertEqual(a, b)

	def test_boolean(self):
		a = True
		b = True
		self.assertEqual(a, b)

def suite():
	"""
	Gather all the tests from this module in a test suite.
	"""
	test_suite = unittest.TestSuite()
	test_suite.addTest(unittest.makeSuite(Testing))
	return test_suite
    
if __name__ == '__main__':
	unittest.main()
