###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=12
#  answer: 76576500

# Pseudocode
# 	- generate next triangle number
# 	- calculate number of divisors
# 	- while number of divisors is equal or less than 500 repeat process
import math

def is_prime(n):
	if n < 2 :
		return False
	if n == 2 :
		return True
	if n % 2 == 0 :
		return False
	s = math.sqrt(n)
	# he says that when we get the squared root, we get the barrier, we will never have two factors bigger that the square root.
	#  That is why, we only have to test smaller numbers than this barrier. We reduce the calculations by 1/2
	k = 3
	while k <= s:
		if n%k == 0:
			return False
		k+=2

	return True

def get_factors(num):

	if is_prime(num):
		return 2;

	div = 2;
	if num == 1:
		div = 1;
	for j in range(1,int(math.sqrt(num))):
		if num%j==0:
			div += 2;
	return div;

def generate_triangle(index):
	#  triangle numbers series: x_n = n*(n+1)/2
	return index*(index+1)/2;

index = 0;
div = 0;
while div<=500:
	index += 1;
	triangle_number = generate_triangle(index);
	# print("Triangle number:", triangle_number)
	div = get_factors(triangle_number);
	print(div);

print(triangle_number);


