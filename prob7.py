# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

#  Boyan Naydenov

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

a = 0;
num = 0;
while a < 10001:
	isPrime = is_prime(num)
	if isPrime:
		a += 1
	num += 1

print(num-1)

