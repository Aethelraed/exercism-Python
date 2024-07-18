def score(x, y):
    r= (x**2+y**2)**0.5
    if r <=1: return 10
    if (r >1) & (r<=5): return 5
    if (r >5) & (r<= 10): return 1
    return 0
