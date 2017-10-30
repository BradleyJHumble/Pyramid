size = input('Please enter the size: ')
chr  = raw_input('Please enter the drawing character: ')

row = 1
while row <= size:
    col = 1
    while col <= row:
        print chr, 
        col = col + 1
    print '' 

    row = row + 1
print ''
