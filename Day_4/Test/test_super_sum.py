'''Test suite for super_sum '''

from unittest import TestCase  #OR import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):  #unittest module has TestCase method  OR .....(unittest.TestCase)
	''' Test case for super sum'''

	def test_empty_input(self):
		''' Test empty input'''
		self.assertEqual(super_sum(), "Please enter an input")  #assert equal comes from TestCase, so when using assertequal you must refernce self i.e.the class
