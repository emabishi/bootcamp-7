'''
Create a class PrimeChecker(number), that takes in a string argument. 
When the instance of the class is called with .is_prime() 
it should return true if number is a prime number and false if it isn't.

'''

class PrimeChecker("string"):
	def __init__(self, string_):
		self.string_ = string_

	def type_cast(self):
		string_ == int

	def is_prime(self):
		if string_ <= 1:
			return False
        if string_ == 3 or string_ == 5 or string_ == 2:
        	return True
        if string_ %2 == 0 or string_ %3 == 0 or string_ %5 == 0 or string_ %7 == 0:
            return False
        if string_ %3 !=0 and string_ %5 !=0:
            return True


x = PrimeChecker("1")
print x.is_prime
