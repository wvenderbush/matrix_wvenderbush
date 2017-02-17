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
	pass




def new_matrix(rows = 4, cols = 4):
	m = []
	for c in range( cols ):
		m.append( [] )
		for r in range( rows ):
			m[c].append( 0 )
	return m


x = new_matrix()
print x
print_matrix(x)
ident(x)
print("\n")
print_matrix(x)
scalar_mult(x, 2)
print("\n")
print_matrix(x)

