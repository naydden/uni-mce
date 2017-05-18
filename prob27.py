#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=27
#  answer: -59231


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

def number_of_primes(a,b):
	n = 0
	while True:
		x = n*n + a*n + b
		if not is_prime(x):
			return n;
		n += 1;

value = {
	'a': 0,
	'b': 0,
	'num_primes': 0
}
for a in range(-999,1000):
	for b in range(-999,1000):
		n = number_of_primes(a,b);
		if value['num_primes'] < n:
			value['a'] = a;
			value['b'] = b;
			value['num_primes'] = n;

print value['a'] * value['b'];