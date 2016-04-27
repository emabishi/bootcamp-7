
'''
#create class HelloAgain
class HelloAgain:
	pass  #ignore this if continuing


#create instance/object of class HelloAgain
x = HelloAgain

'''
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



#--------------------end of class

p = Person('Jonah', 23)   #made an instance
p1 = Person("Mark", 44)
p2 = Person("Thomas", 22)

print("------------")

print p.say_Hello()

print "--------------------"

print Person.people_count
print p2.people_count

print "-------------------"

a = [ ('Jane', 23), ('Joe', 50), ('Jackie', 34), ('Jacob',23), ('Jee', 25), ('Josh', 30)
    ]

new_list  = []
for name, age in a:
	x = Person(name, age)  #go through a and store each object in new_list
	new_list.append(x)

for w in new_list:
	print w.say_Hello()

print "-----------"

