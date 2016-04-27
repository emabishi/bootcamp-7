f = [(10,20,30), (10,20), (50,60,70)]


print len(f)
for x in f:
	print len(x)

print "-----------------"

for x,y,z in f:
	if len(x) == 2:
		print "x: {}, y: {}, z: {}".format(x,y)
	print "x: {}, y: {} , z: {}".format(x,y,z)
