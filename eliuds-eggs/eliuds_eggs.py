import math
def egg_count(display_value):
    if display_value < 1: return display_value
    n,out = math.floor(math.log(display_value,2)), 0
    while n > -1:
        out,n, display_value= out+1 if 2**n <= display_value else out, n-1, display_value - 2**n if 2**n <= display_value else display_value
    return out