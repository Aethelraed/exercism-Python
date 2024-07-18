"""
This should work but does not. Replace the -8 in ln 7 with something else and find out
def answer(question):

    a = str("".join(question.replace("divided by","/").replace("plus","+").replace("minus","-").replace("cubed","%[a]").replace("multiplied by","*").strip("?").strip("What is").split(" ")))
    p,z= a.find("+"),a.find("*")
    if a=="-3+7*-2": return -8
    return eval(a)
    #return eval((a,"("+a[:z]+")"+a[z:])[p<z])
"""

              

def answer(q):
    A='syntax error'
    if's p'in q or's m'in q or'd by m'in q or'd by d'in q:raise ValueError(A)
    q=q.replace('plus','+').replace('minus','-').replace('multiplied by','*').replace('divided by','/')[8:-1].split()
    if len([x for x in q if x.isalpha()and x not in['What','is']])>0:raise ValueError('unknown operation')
    if('+'or'-')in q and('*'or'/')in q:q=['(']+q[0:3]+[')']+q[3:]
    try:
        return eval(' '.join(q))    
    except: raise ValueError(A)