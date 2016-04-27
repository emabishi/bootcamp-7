# unpacking
def hello(name, age, class_=''):
    '''
    Explains how to unpack lists
    '''
    if class_ != '':
        return "I am {}, {} y/o, and {} class".format(name, age, class_)
    return "I am {}, and I'm {}".format(name, age)


people = [
            ("Jane", 23, 'High'),
            ("Joe", 25, 'Low'),
            ("Brian", 60),
            ("Betty", 45)
            ]

# for name, age in people:
#     print hello(name, age)

# use of unpacking

for x in people:
    print hello(*x)
print "-----------"

def super_sum(*args):   #take an undefined number of arguments
    '''
    Takes in variable number of items, and returns the sum.
    e.g super_sum(10,20) = 30
    '''
    
    total = 0
    for i in args:
        total += i
    return total


print super_sum(10,20)
print "---------------"

a = [10,20,30,40]
print super_sum(*a)  #unpack list a and put those elements as the arguments to the function

print "------------"

def super_sum(a, b , *args):   #take an undefined number of arguments but a minimum of two
    '''
    Takes in variable number of items, and returns the sum.
    e.g super_sum(10,20) = 30
    '''
    
    total = 0
    for i in args:
        total += i
    return total + a + b  #remember to add a and b to total


print super_sum(10,20)  #Remember, super_sum will fail if you provide less than 2 arguments
print "---------------"

a = [10,20,30,40]
print super_sum(*a)  #unpack list a and put those elements as the arguments to the function

print "===================="

def hello_again(**kwargs):
    return "I am {} and I am {} y/old".format(kwargs['name'], kwargs['age'])

print hello_again(name='Joe',age=23)
print hello_again(age=20,name='Jonah')

#unpack other_people list dictionary
other_people = [ {'name' : 'Joe' , 'age': 98},
                 {'name': 'Jane', 'age': 60},
                 {'name': 'Trump', 'age' : 23}
               ]

for x in other_people:
    print hello_again(**x)

print "---------------"
#unpack dictionary joes
joe = {'name': 'Joe', 'age': 98}

print "----------------"
print hello_again(**joe)   # same as saying what's below
print hello_again(name='Joe', age=98)

