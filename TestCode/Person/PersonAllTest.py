import unittest
import PersonBTest; 
import PersonTest;

if __name__ == '__main__':
	PersonBTestSuite = PersonBTest.suite();
	PersonTestSuite = PersonTest.suite();
	runner=unittest.TextTestRunner()
	runner.run(PersonBTestSuite)
	runner.run(PersonTestSuite)
	