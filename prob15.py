###########  Boyan Naydenov  #############
#  https://projecteuler.net/problem=15
#  answer: 137846528820


import math

grid = input("What is the squared grid size? ")
print("Grid size: " + str(grid) + "x" + str(grid));

number_routes = math.factorial(grid*2)/(math.factorial(grid)*math.factorial(grid));

print("Number of possible routes to arrive to the end:" + str(number_routes));