#import math functions from math module
from math import*

def polysum(n, s):
    """
    input: number of sides, integer n
            length of sides, integer s
    output: gives out the sum of perimeter squared and the area up to 4 decimal places
    """
    #using given formula to calculate area
    area = (.25 * n * s**2)/tan(pi/n)

    #using known perimeter formula to evalute perimeter of polygon
    perimeter = n * s
    
    #return statement with round() method to get up to 4 decimals
    return round(perimeter**2 + area, 4)
