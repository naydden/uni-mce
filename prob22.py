#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=22
#  answer: 871198282

import re

with open('p022_names.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

array = sorted(data.split(","))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
def get_score(name):
	score = 0;
	for l in name:
		if l == '"':
			continue
		else:
			score += alphabet.index(l.lower())+1;
	return score;

result = 0
for i in range(len(array)):
	result += (i+1)*get_score(array[i])

print result