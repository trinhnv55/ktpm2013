#Determine if input is a triangle using triangle inequality function
def is_triangle(a, b, c):
    return True if (a < b + c and b < a + c and c < a + b) else False

def is_equilateral(a, b, c):
    return True if (a == b == c) else False

def is_isosceles(a, b, c):
    return True if a == b or b == c or a == c else False

#Triangle determiner:
# Input: length of the 3 edges
# Output: Not a triangle | type of triangle

def main(a, b, c):
    '''
    a:[0;10][31;40][10;30]
    b:[0;5][7;20][25;30]
    c:[0;7][10;25][26;50]
    '''

    if is_triangle(a, b, c):
        if is_equilateral(a, b, c):
            return 'Equilateral triangle'
        elif is_isosceles(a, b, c):
            return 'Isosceles triangle'
        else:
            return 'Triangle'
    else: return 'Not a triangle'
