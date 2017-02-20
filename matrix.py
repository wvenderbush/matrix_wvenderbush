import math


def print_matrix( matrix ):
	for row in matrix:
		group = []
		group.append("|")
		for val in row:
			group.append(str(val));
			group.append(" ")
		group[-1] = "|"
		print("".join(group))

def ident( matrix ):
	count = 0
	for val in matrix:
		incount = 0;
		while (incount < len(val)):
			val[incount] = 0
			incount += 1
		val[count] = 1
		count += 1


def scalar_mult( matrix, s ):
	for val in matrix:
		incount = 0;
		while (incount < len(val)):
			val[incount] = val[incount] * s
			incount += 1

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	rows1 = len(m1)
	cols1 = len(m1[0])
	rows2 = len(m2)
	cols2 = len(m2[0])
	if (cols2 != rows1 or rows2 != cols1):
		return []
	else:
		retrix = [[0 for row in range(cols2)] for col in range(rows1)]
		for i in range(rows1):
			for j in range(cols2):
				for k in range(cols1):
					retrix[i][j] += m1[i][k] * m2[k][j]
	return retrix



def new_matrix(rows = 4, cols = 4):
	m = []
	for c in range( cols ):
		m.append( [] )
		for r in range( rows ):
			m[c].append( 0 )
	return m

