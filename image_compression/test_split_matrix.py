import math
from split_matrix import split_matrix
#  generation of a matrix with m and n not being powers of 2
m = [[1 for col in range(2037)] for row in range(3135)];

num_rows = range(int(math.ceil(len(m)/16.0)));
rows = [x * 16 for x in num_rows];

num_columns = range(int(math.ceil(len(m[0])/16.0)));
columns = [x * 16 for x in num_columns];

for i in rows:
	for j in columns:
		print len(split_matrix(m,i,j)), len(split_matrix(m,i,j)[0])
		print split_matrix(m,i,j)