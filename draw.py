from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    count = 0;
    while (count < len(matrix) - 1):
        p1 = matrix[count]
        p2 = matrix[count + 1]
        draw_line(p1[0], p1[1], p2[0], p2[1], screen, color)
        count += 2


def add_point( matrix, x, y, z=0.0 ):
    pointlen = len(matrix[0])
    for point in matrix:
        if (point[pointlen - 1] == 0):
            point[0] = x * 1.0
            point[1] = y * 1.0
            point[2] = z * 1.0
            point[3] = 1.0
            return matrix
    adlist = [x * 1.0, y * 1.0, z * 1.0, 1.0]
    matrix.append(adlist)
    return matrix


def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    return matrix


def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line



