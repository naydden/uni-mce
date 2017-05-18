#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=26
#  answer: 983

size = 0;
result = 0;
sizes = [];
d = range(1,1000);
for i in d:
	previous_reminders = [];
	reminder = 1;
	size = 0;
	while True:
		size += 1;
		previous_reminders.extend([reminder]);
		if size == 1:
			reminder = 1.0%i;
		else:
			reminder = (reminder*10)%i;
			# if reminder already existed, then we hit the end of the cycle
			#  also if size reaches i-1 level, we can stop since there will be no more
			if reminder in previous_reminders or size == (i-1):
				break;
	sizes.extend([size]);

print d[max(sizes)]