###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=16
#  answer: 1366

import math

number = int(math.pow(2, 1000));


string = str(number);

string = map(int, list(string));

summ = 0
for i in range(len(string)):
	summ += string[i];

print(summ);