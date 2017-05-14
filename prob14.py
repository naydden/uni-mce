###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=14
#  answer: 837799

# Pseudocode
#  start from 2
#  a function to determine if it is odd
#  a function to determine if it is even
#  a function that does Collatz sequence
# and a counter is counting the number of
#  iterations until arriving to 1 and saving initial value

def is_even(num):
	if num%2 == 0:
		return True;
	return False;

def collatz(num):
	counter = 0;
	while (num!=1):
		if is_even(num):
			num = num/2 ;
		else:
			num = 3*num + 1;
		counter += 1;
	return counter;

max_value = 0;
max_counter = 0;
max_value = 0;

for i in range(2,1000000+1):
	counter = collatz(i);

	if counter > max_counter:
		max_counter = counter;
		max_value = i;

print(max_value);