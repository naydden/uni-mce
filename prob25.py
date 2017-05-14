#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=25
#  answer: 4782

f_1 = 1;
f_2 = 1;
n = 2;
digits = 0
while digits<1000:
	n+=1;
	f = f_1 + f_2;
	f_2 = f_1;
	f_1 = f;
	digits = len(str(f));

print n