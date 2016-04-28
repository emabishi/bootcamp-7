'''
You are presented with a string or a collection of strings

Your function should return the length of the string, or strings in a list

['Fairy', 'tale'] should return [5, 4]

'C-sharp' should return [7]

'''


def string_length(x):

	list_for_string = []
	
	if type(x) == str:
		r = len(x)
		list_for_string.append(r)
		return list_for_string

	list_for_list = []
	for a in x:
		v =len(a)
	 	list_for_list.append(v)
	return list_for_list

						
print string_length("Potassium")
print string_length(['Adam', 'Frankel'])



