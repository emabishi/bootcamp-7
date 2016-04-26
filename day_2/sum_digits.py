def sum_digits(A):
	'''
	Takes a list and returns the sum of all the sum_digits
	in the list
	'''
	total = 0
    for x in A:
      p = int(x)
    #print(p)
      total += p
    return total