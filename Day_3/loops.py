
a = [10,30,22,50,67,99]
b = [(2,4),(5,10), (6,20), (5,50)]
c = [(2,3,4), (10,20,30)]

#for loop example
for i in a:
	print i

#print in reverse
#Method 1
i = len(a)

while i > 0:
	print a[i-1]
	i -=1
	
# Method 2
for index in range(len(a)-1, -1, -1):
	print a[index]

for x,y in b:
	print "x: {}, y: {}". format(x,y)
#OR
print("=======")
for x,y in b:
	print "x: ", x , "y: ", y
#Or for 3Dimensions
print("--------")
for x,y,z in c:
	print "x:", x , "y:", y , "z:", z