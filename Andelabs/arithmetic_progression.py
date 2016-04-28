'''
You are required to check if the array passed as an argument is 
arithmetic, geometric, neither arithmetic nor geometric in progression or if the array is empty.

For arithmetic progressions, return Arithmetic
For geometric progressions, return Geometric
For neither of the above, return -1
For an empty array, return 0
'''
'''
def check_progression(x):
	type(x) == list
	count = 0
	while len(x) >= 0:
			return "Arithmetic"
'''


def is_arithmetic(l):

    if len(l) == 0:
        	return 0
    #delta = l[1] - l[0]
    for index in range(len(l) - 1): 	
        if (l[index + 2] - l[index + 1] == l[index + 3]  - l[index + 2]):
        	return "Arithmetic" ##correct
        elif (l[index + 1] / l[index]) == (l[index + 2] / l[index + 1]):
        	return "Geometric"
        else:
        	return -1

print is_arithmetic([])
print is_arithmetic([2,4,6,8])
print is_arithmetic([2,6,18,54,162])
print is_arithmetic([15, 10, 5, 0, -5, -10])
print is_arithmetic([0.5, 3.5, 24.5, 171.5])
print is_arithmetic([1, 2, 3, 5, 8])
print is_arithmetic([-1, -8, -27, -64, -125])