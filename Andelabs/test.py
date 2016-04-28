a = (["Fairy", "Tale"])

newlist = []
for x in a:
	 v = len(x)
	 newlist.append(v)
	 print newlist

a = []
print len(a)

def arg_len(x,y,z):
	print len(x)
	print len(y)
	print len(z)

arg_len([1,2,3], [1,4,5], [1.2])