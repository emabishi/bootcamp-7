from person import Person  #from person file import Person class
from kenyan import Kenyan   #import Kenyan class from kenyan file

'''
#create class HelloAgain
class HelloAgain:
	pass  #ignore this if continuing


#create instance/object of class HelloAgain
x = HelloAgain

'''

#--------------------tests

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

k = Kenyan("Miguna", 50)

k.probe(True)
print "Is {}, corrupt? {}".format(k.name, k.is_corrupt())

print k.say_Hello()

print "-----"
print k.say_Hello() + " and " + k.is_corrupt()