'''
Output: x: 10, y: 20, z: 30
        x:  10, y: 20
        x:  50, y:  60, z: 70
'''

f = [(10,20,30), (10,20), (50,60,70)]

print len(f)
print "-----------"

for e in f:
	print len(e)

print "---------"


for e in f:
	if len(e) != 3:
		print "z : 0"
	else:
		print "Has z coordinate"

print "------------"


for e in f:
	for x,y,z in f:
		print "x:", x , "y:", y , "z:", z	
	if len(e) !=3:
		print "z : 0"




		








