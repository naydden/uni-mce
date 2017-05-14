import math

def sum_of_proper_divisors(n):
	sum = 0;
	for i in range(1,n/2+1):
		if n%i == 0:
			sum += i;
	return sum;
	# ========= A better way
	# sum = 1
	# i = 2
	# s = math.sqrt(n)
	# while i <= s:
	# 	if n % i == 0:
	# 		sum += 1
	# 		if i**2 != n:
	# 			sum += n/i;
	# 	i += 1
	# return sum;