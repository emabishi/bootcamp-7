
def super_sum(*args):
	'''
	Return sum of numbers.
	e.g.
	super_sum() === "Please enter an input"
	super_sum(1,2,3) === 6
	super_sum([1,2,3]) === 6
	super_sum([10], [20,30]) === 60    i.e. many lists
	'''
	total = 0
	if not args:   #No argument i.e. super_sum(0)
		return 0
	else:
		for x in args:   #Unpacking args will return a tuple
			if type(x) == list:
				total += sum(x)   #+ because args may be lists and integers
				#------OR
				#for i in x:
					#total += i
			elif type(x) == str:
				return 0
			else:
				total += x
		return total

