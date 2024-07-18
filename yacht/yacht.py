# Score categories.
YACHT = lambda x: 50 if all(x[0]==d for d in x) else 0
ONES = lambda x: sum(d==1 for d in x)
TWOS = lambda x: 2*sum(d==2 for d in x)
THREES = lambda x: 3*sum(d==3 for d in x)
FOURS = lambda x: 4*sum(d==4 for d in x)
FIVES = lambda x: 5*sum(d==5 for d in x)
SIXES = lambda x: 6*sum(d==6 for d in x)
FULL_HOUSE = lambda x: sum(x) if all(len(set(x[i:i+4]))==2 for i in [0,1]) else 0 
FOUR_OF_A_KIND = lambda x: 4*x[0] if sum(len(set(sorted(x)[i:i+4]))==1 for i in [0,1]) >0 else 0 #TODO 20% chance of guessing wrong
LITTLE_STRAIGHT = lambda x: 30 if sorted(x)==[1,2,3,4,5] else 0
BIG_STRAIGHT = lambda x: 30 if sorted(x)==[2,3,4,5,6] else 0
CHOICE = sum

score = lambda dice, category: category(dice)