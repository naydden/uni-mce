#  function receives a matrix and indexes.
#  the indexes mark where we start the submatrix of 16x16
#  the aim is to have a matrix with m and n multiple of 2
#  in order to efficiently perform the Haar transform

def split_matrix(m,i,j):
	#  let's create a 16x16 matrix full of zeros.
	submatrix = [[0 for col in range(16)] for row in range(16)];
	em = 0;
	en = 0;
	for k in range(i,i+16):
		for l in range(j,j+16):
			if k > (len(m) - 1) or l > (len(m[0]) - 1):
				en += 1;
				break;
			submatrix[em][en] = m[k][l];
			en += 1;
		# print submatrix
		em += 1;
		en = 0;
	return submatrix;