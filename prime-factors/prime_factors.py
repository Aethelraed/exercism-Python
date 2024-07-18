def factors(value):
    out,d = [],2
    while value >1:
        if value % d ==0:
            out += [d]
            value = value / d
        else:
            d +=1
    return out