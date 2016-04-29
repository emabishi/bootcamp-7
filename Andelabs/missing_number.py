'''

You are presented with two arrays, all containing positive integers. One of the arrays will have 
one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77

'''
'''
def arg_len(x,y):
	#print len(x)
	#print len(y)
	#print len(z)
	if len(y) > len(x):
		print set(y).difference(x)
	elif len(x) == 0:
		return 0
	elif sum(x) == sum(y):   #there are exceptions to this. Not pythonic!
		return 0
	else:
		return set(x).difference(y)
		 
print arg_len([1,2,3],[2,6,8])

'''

def find_missing(A, B):
  if len(A) == len(B):
    return 0 
  else:
      for x in B:
        if x not in A:
          return x


