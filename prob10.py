###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=10
#  answer: 142913828922


import math

def is_prime(n):
	if n < 2 :
		return False
	if n == 2 :
		return True
	if n % 2 == 0 :
		return False
	s = math.sqrt(n)
	# he says that when we get the squared root, we get the barrier, we will never have two factors bigger that the square root.
	#  That is why, we only have to test smaller numbers than this barrier. We reduce the calculations by 1/2
	k = 3
	while k <= s:
		if n%k == 0:
			return False
		k+=2

	return True

prime = 1;
sumofprimes = 0;
num = 0;

while prime < 2000000:
	if is_prime(num):
		if num < 2000000:
			sumofprimes += num
		prime = num
	num += 1

print(sumofprimes)