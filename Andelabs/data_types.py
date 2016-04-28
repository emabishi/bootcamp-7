'''
Define a function called data_type, to take one argument. 
Compare and return results, based on the argument supplied to the function. 
Complete the test to produce the perfect function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred 
e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist
'''

def data_type(x):
	if type(x) == str:
		return len(x)
	if x is None:
		return "no value"
	if type(x) == bool:
		return x
	if type(x) == int:
		if x < 100:
			return "less than 100"
		if x == 100:
			return "equal to 100"
		else:
			return "more than 100"
	if type(x) == list:
		if len(x) >= 3:
			return x[2]
		else:
			return None



print data_type(3)
print data_type("Potassium")
print data_type("")
print data_type([1,3,4])
print data_type([1,2])
print data_type(True)


