f = [(10,20,30), (10,20), (50,60,70)]

print len(f)
print "-----------"

for e in f:
	print len(e)

print "---------"


'''

for x,y,z in f:
	if e in f:
		if len(e) < 3:
			print "x: {}, y: {}, z: {}".format(x,y)
			print "x: {}, y: {} , z: {}".format(x,y,z)
	else:
		print("Okay")

print "-----------------"

'''

for x,y,z in f:
	if len(x) == 2:
		print "x: {}, y: {}, z: {}".format(x,y)
	print "x: {}, y: {} , z: {}".format(x,y,z)
'''