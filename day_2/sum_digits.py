def sum_digits(A):
	'''
	Takes a list and returns the sum of all the sum_digits
	in the list
	'''
	total = 0
	for x in A:
		type(x) == int
		total += x
	return total

#test your code

print sum_digits([1,2,3,4])
