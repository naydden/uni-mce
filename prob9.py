###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=9
#  answer: 31875000

import math
def theOne(a,b):

	x = a*a + b*b
	if isinstance(x,int):
		c = math.sqrt(x)
		#  Check if c is a natural number
		if c-int(c) == 0:
			if a+b+c == 1000:
				print(a*b*c)
				return True
	return False


found = False
a = 1
b = 1

def iterate():
	# Range till 999 becauase it can't be bigger, since the sum of the three numbers is 1000
	for i in range(1,999):
		for j in range(i,999):
			found = theOne(i,j)
			if found:
				return

iterate()

