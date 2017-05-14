#!/usr/bin/python
###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=17
#  answer: 21124

# pseudocode
#  1. Iterate over numbers from 1 to 1000
#  2. Function to return the number written in text when we pass to it a number.
#  3. Iteration counts lenght of string, without counting spaces!! And adds result to global counter

units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

first_tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def num_to_text_tens(num):
	if num < 10:
		string = units[num-1];
	elif num >= 10 and num < 20:
		units_number = num%10;
		string = first_tens[units_number];
	elif num < 100:
		tens_number = num/10;
		units_number = num%10;
		if units_number != 0:
			string = tens[tens_number-1] + "-" + units[units_number-1];
		else:
			string = tens[tens_number-1];
	return string;

def num_to_text_hundreds(num):
	print num;
	hundreds_number = num/100;
	tens_number = num - hundreds_number*100;
	if num%100 == 00:
		string = units[hundreds_number-1] +" hundred";
	else:
		string = units[hundreds_number-1] +" hundred and "+ num_to_text_tens(tens_number);
	return string;
def char_counter(string):
	print string
	counter = 0;
	for l in string:
		if l!= " " and l!= "-":
			counter += 1;
	print counter
	return counter;


letters_counter = 0;
for i in range(1,1001):
	if i==1000:
		string = "one thousand";
	elif i<100:
		string = num_to_text_tens(i);
	else:
		string = num_to_text_hundreds(i);

	letters_counter += char_counter(string);

print letters_counter;