import math[]


def print_matrix( matrix ):
    for row in matrix:
    	for val in row:
    		print val


def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    colcount = 0

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
print new_matrix
