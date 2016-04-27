#global variable
people = [
('Joe', 78), 
('Janet', 29),
('Ana', 10)
           ]



def super_sum(*args):
	return sum(args)

def hello_again(name,age):
	return "I am {} and {} years old".format(name,age)

def max_min(A):
	'''
	Returns max(A) - min(A)
	'''
	max_ , min_ = A[0] , A[0]   #unpacking A

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			min_ = i

	return max_ - min_