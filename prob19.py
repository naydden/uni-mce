#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=19
#  answer:  171
import datetime

counter = 0;
for year in range(1901,2001):
	for month in range(1,13):
		if datetime.date(year, month, 1).ctime()[:3] == "Sun":
			counter += 1;
print counter;