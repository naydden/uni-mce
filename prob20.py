#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=20
#  answer: 648

def factorial(num):
	if num!= 1:
		return num * factorial(num- 1);
	else:
		return num;

array = map(int,list(str(factorial(100))));

print sum(array);