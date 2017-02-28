from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


#print_matrix(matrix)

#Identity Matrix
print "\nID Matrix\n"
idmatrix = new_matrix()
ident(idmatrix)
print_matrix(idmatrix)

#Scalar Multiplication
print "\nScalar Multiplication by 2\n"
print_matrix(idmatrix)
print "(x2) becomes..."
scalar_mult( idmatrix, 2 )
print_matrix(idmatrix)

#Matrix Multiplication
print "\nMatrix Multiplication\n"
w, h = 4, 4;
m1 = [[random.randrange(0, 10)*(1.0) for x in range(w)] for y in range(h)] 
m2 = [[random.randrange(0, 10)*(1.0) for x in range(w)] for y in range(h)] 
print "M1"
print_matrix(m1)
print "\nM2"
print_matrix(m2)
print "\nM1 x M2 Result"
print_matrix(matrix_mult(m1, m2))





#Generating Image with Matrix

add_edge( matrix, 250, 0, 0, 500, 250, 0)
add_edge( matrix, 250, 500, 0, 500, 250, 0)
add_edge( matrix, 0, 250, 0, 250, 0, 0)
add_edge( matrix, 0, 250, 0, 250, 500, 0)

add_edge( matrix, 0, 0, 0, 500, 500, 0)
add_edge( matrix, 0, 500, 0, 500, 0, 0)

add_edge( matrix, 250, 0, 0, 250, 500, 0)
add_edge( matrix, 0, 250, 0, 500, 250, 0)

add_edge( matrix, 125, 0, 0, 375, 500, 0)
add_edge( matrix, 125, 500, 0, 375, 0, 0)

add_edge( matrix, 0, 375, 0, 500, 125, 0)
add_edge( matrix, 0, 125, 0, 500, 375, 0)

print "\n\n\n"
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
