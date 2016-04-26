def super_sum(A):
	'''
	Takes in a list A and halves every even number while doubling every odd.
	Returns the sum of all
	'''
	total = 0
	for item in A:
		if (item % 2) == 0:
			total += (item/2)
		else:
			total += (item*2)  #total = total + item * 2

	return total

#super_sum([1,2,3,10,20,30])




