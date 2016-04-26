def sum_elements(A):
	'''
	Sum each element within a list i.e.
	for A = [11,22,33,44] output 1+1+2+2...
	'''
	total = 0
	for x in A:
		y = str(x)  # change the elements in A into strings
		for m in y:
			b = int(m)  #change the sstrings into integers
			total += b
	return total          
    
#test
print sum_elements([11,22,33])