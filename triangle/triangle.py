def equilateral(sides):    return ((sum(sides)>1) & (sides[1]==sides[2]) & (sides[1] == sides[0]))


def isosceles(sides):    return ((sum(sides)>1) & ((sides[0]==sides[1])|(sides[1]==sides[2] ) | (sides[2] == sides[0]))&((max(sides)/sum(sides))<0.5))


def scalene(sides):    return ((sum(sides)>1) & ((sides[1]!=sides[2] ) & (sides[2] != sides[0])& (sides[1] != sides[0]))&((max(sides)/sum(sides))<0.5))
