'''Test suite for super_sum '''

from unittest import TestCase  #OR import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):  #unittest module has TestCase method  OR .....(unittest.TestCase)
	''' Test case for super sum'''

	def test_empty_input(self):
		''' Test empty input'''
		self.assertEqual(0,super_sum())  #assert equal comes from TestCase, so when using assertequal you must refernce self i.e.the class
	
	def test_sum_of_integers(self):
		'''Test sum of integers'''
		self.assertEqual(super_sum(1, 2, 3), 6)  #+ve and +ve
		self.assertEqual(super_sum(-1, 1), 0)    #-ve and positive number
		self.assertNotEqual(super_sum(10,20,30), 100)

	def test_sum_of_strings(self):
		self.assertEqual(super_sum("string",1,4),0)

	def test_sum_of_elements_in_one_list(self):
		'''Test sum of items in a single list'''
		self.assertEqual(super_sum([1,2,3]), 6)