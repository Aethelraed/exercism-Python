def square_root(number):
    n = max((1,number // 2))
    while n **2 > number: n = n-1
    return n
