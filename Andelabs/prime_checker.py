'''
Create a class PrimeChecker(number), that takes in a string argument. 
When the instance of the class is called with .is_prime() 
it should return true if number is a prime number and false if it isn't.

'''
'''
class PrimeChecker("string"):
	def __init__(self, string_):
		self.string_ = string_

	def type_cast(self):
		string_ == int

	def is_prime(self):
		if string_ <= 1:
			return False
        elif string_ == 3 or string_ == 5 or string_ == 2:
        	return True
        elif string_ %2 == 0 or string_ %3 == 0 or string_ %5 == 0 or string_ %7 == 0:
            return False
        elif string_ %3 !=0 and string_ %5 !=0:
            return True


x = PrimeChecker("1")
print x.is_prime
'''

'''
class PrimeChecker(object):

 def __init__(self, number=""):
  self.number = number

 def is_prime(self):

    if self.number != '':
     x = int(self.number)
     if x <= 1:
      return False 
     else:
       for i in range(2,x):
        if x % i == 0:
         return False
        return True 
    else:
     return False

'''
'''
class PrimeChecker(object):

 def __init__(self, number=""):
  self.number = number

 def is_prime(self):

    if self.number != '':
     x = int(self.number)
     if x <= 1:
      return False 
     else:
       for i in range(2,x):
        if x % i == 0:
         return False
        return True 
    else:
     return False

'''
class PrimeChecker(object):
	def __init__(self, number = ""):
		self.number = number


	def is_prime(self):
		if self.number <= 1:
			return False
        if self.number == 3 or self.number == 5 or self.number == 2:
        	return True
        if self.number %2 == 0 or self.number %3 == 0 or self.number %5 == 0 or self.number %7 == 0:
            return False
        if self.number %3 !=0 and self.number %5 !=0:
            return True
       



x = PrimeChecker(10)
print x.is_prime()

y = PrimeChecker(1)
print y.is_prime()

r = PrimeChecker(7)
print r.is_prime()