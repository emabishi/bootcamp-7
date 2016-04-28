'''
You are to write a function, reverse_string(string), 
that returns the reverse of the string provided. 
If the reverse of the string is the same as the original string, 
as in the case of palindromes, return true instead.
For empty string return 'None'
'''
'''
def reverse_string(A=None):
  
	x = A[::-1]
	
	if A == ' ':   #empty string
		return 'None'
	elif A != x:
		return x  #return reverse
	
	elif A == x:   #palinadrome
		return "true"


'''
def reverse_string(A):
  
	x = A[::-1]
	
	if A == '' and A != x:
		return 'None'
	elif A != x:
		return x
	
	elif A == x and A is not '':
		return "true"



print reverse_string("111")
print reverse_string("1234")
print reverse_string(" ")