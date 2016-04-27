def data_type(x):
	'''
	Takes in argument, x:
	-For an integer, return double integer
	-For float, return half float
	-For string, return "Hello" + string
	-For boolean, return string "boolean"
	-For long, return sqrt of long
	'''
	try:
	    if type(x) == int:
		  return (x*2)
	    elif type(x) == float:
		  return (x/2)
	    elif type(x) == str:
		  return "Hello " + x   #OR return "Hello {}".format(x)
	    elif type(x) == bool:
		  return "boolean"
	    elif type(x) == long:
		  return "long"
	except NameError:
		return  "Please enter valid data type"

#test
print data_type(2)
print data_type(3.141)
print data_type("Potassium")
print data_type(True)
print data_type(22298989848899912345467891234567892231456890)
print data_type(tghy6)   #Exception causing  error, not handled, unsure of reason

