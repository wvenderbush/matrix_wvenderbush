from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()



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

print_matrix(matrix)



draw_lines( matrix, screen, color )
display(screen)
