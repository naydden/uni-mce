#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=23
#  answer:

# Pseudocode
# iterate numbers from 12 to  28123
# in each iteration  call sum_of_of_divisors and check if it is abundant
# if it is abundant save
# sum_of(1:23) + all the num<28123 that can't be expressed as a sum_of of two abundant numbers

from Divisors import sum_of_proper_divisors


d = range(12,28123+1);
abundant = [];
for i in d:
	if sum_of_proper_divisors(i) > i:
		abundant.extend([i]);

sum_of = [];
len_abundant = len(abundant);
activated = False
for i in range(len_abundant):
	if i == len_abundant:
		sum_of.extend([abundant[i]+abundant[i]]);
		break
	for j in range(i,len_abundant):
		summ = abundant[i]+abundant[j];
		if summ > 28123:
			print('BREAKK')
			break;
		elif summ in sum_of:
			continue;
		else:
			sum_of.extend([summ]);


result = 0;
print len(sum_of)
for i in range(1,28123+1):
	if i in sum_of:
		continue;
	else:
		result += i;
print result;

