def triplets_with_sum(number):
    out = []
    for j in range(number//4,number//2):
        for i in range(number//4,j):
            a,b,c = sorted((i,j,number-i-j))
            if (a)**2+(b)**2 == (c)**2 and not [a,b,c] in out: out.append([a,b,c])

    return sorted(out)


