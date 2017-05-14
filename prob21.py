#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=21
#  answer: 31626

from Divisors import sum_of_proper_divisors

result = 0
d = range(0,10000);

d = map(sum_of_proper_divisors,d);

for i in xrange(1,10000):
	for j in xrange(i+1,10000):
		if d[i] == j and d[j] == i:
			result += i+j

print "The sum of amicable numbers is: %d" % result;