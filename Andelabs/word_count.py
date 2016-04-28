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
	x = string.split()   #split into list
	count = {}
	for word in x:     #x in list_
		if word in count:  #
			count[word] += 1
		else:
			count[word] = 1
	for i in count:
		print i, ":", count[i]


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
		print i, ":", count[i]

'''
wordslist = wordlst.split()

dict_ = {}

for word in wordslist:
    if word.isdigit():
        word = int(word)
    if word in dict_:
        dict_[word] = dict_[word] + 1
    else:
        dict_[word] = 1

return dict_


'''


print word_count("olly olly in come free")
print word_count('word')
print word_count("one of each")
print word_count('one fish two fish red fish blue fish')
print word_count('car : carpet as java : javascript!!&@$%^&')
print word_count('testing 1 2 testing')
print word_count('go Go GO')
print word_count('¡Hola! ¿Qué tal? Привет!')
print word_count('hello\nworld')
print word_count('hello\tworld')
print word_count('hello  world')



