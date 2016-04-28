'''
Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

        N is an integer within the range [1..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1).
'''

def solution(N):
		bin_ = '{0:08b}'.format(N)   #binary value of N
		print bin_

		count_0 = 0
		count_1 = 0
		bin_ = str(bin_)
		#print len(bin_)
		for x in range(len(bin_)):
			if x == str(0):
				count_0 += 1	
			elif x == str(1):
				count_1 += 1
		print count_1
		print count_0




	
solution(23)