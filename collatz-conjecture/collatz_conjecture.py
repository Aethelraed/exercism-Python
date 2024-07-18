def steps(number):
    if number <1: raise ValueError("Only positive integers are allowed")
    n = 0
    while number >1:
        n = n+1
        if number % 2 == 1: number = number*3+1            
        elif number % 2 == 0: number = number /2            
    return n