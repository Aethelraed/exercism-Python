def score(word):
    values = dict.fromkeys("A,E,I,O,U,L,N,R,S,T".split(","),1)|dict.fromkeys("D,G".split(","),2)|dict.fromkeys("B,C,M,P".split(","),3)|dict.fromkeys("F,H,V,W,Y".split(","),4)|dict.fromkeys("K".split(","),5)|dict.fromkeys("J,X".split(","),8)|dict.fromkeys("Q,Z".split(","),10)
    return sum(values[w] for w in word.upper())
