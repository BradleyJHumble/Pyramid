def triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print ' ' * ( t + 1 ) + '*' * ( i * 2 - 1 )
        return triangle( i - 1, t + 1 )
triangle(5)
