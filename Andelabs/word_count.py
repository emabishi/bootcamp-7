'''
For example for the input "olly olly in come free"

olly: 2
in: 1
come: 1
free: 1

'''

'''
def word_count(string):
	x = string.split()
	#print type(x)
	for a in x:
		#print a
		print a, ": ",len(a)



def word_count(string):
	x = string.split(' ')
	#print type(x)
	for a in x:
		if x.count(a) > 1:
		print x.count(a)

'''

'''
def word_count(string):
	words_ = string.split()  
	count = {}
	for word in words_:     
		if word in count:  
			count[word] += 1
		else:
			count[word] = 1
		#if type(string) == type(unicode):
			#count[word] += 1
	for i in count:
		print i,":",count[i]

'''
def words(A):
  dictionary = {}
  
  for i in A.split():
    if i.isdigit():
      i = int (i)


    if i in dictionary:
      dictionary[i]  += 1
    else:
      dictionary[i] = 1
      
  return dictionary


print word_count("olly olly in come free")
print word_count('word')
print word_count("one of each")
print word_count('one fish two fish red fish blue fish')
print word_count('car : carpet as java : javascript!!&@$%^&')
print word_count('testing 1 2 testing')
print word_count('go Go GO')

print word_count('hello\nworld')
print word_count('hello\tworld')
print word_count('hello  world')



