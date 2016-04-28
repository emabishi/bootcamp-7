'''
Your answer should be returned in an array 
containing the min and max number, respectively.

'''

def find_max_min(A):
	newlist = []
	newlist2 = []
	x = max(A)
	y = min(A)
	if x == y:
	  newlist2.append(len(A))
	  return newlist2
	else:
		newlist.append(y)
		newlist.append(x)
		return newlist

