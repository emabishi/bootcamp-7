


class Person:

	#class variable
	people_count = 0

	def __init__(self, name, age):  #run this initially, ususally implicity run when python encounters object instance
	#instance variable
	  Person.people_count += 1   #increment counter every time init runs at the beginnin gof this class

	  self.name = name
	  self.age = age

	def __repr__(self):
		return "<object: {}, {}". format(self.name, self.age)

	def say_Hello(self):
		return "Hello, I am {} and {} y/old".format(self.name, self.age)