from re import sub,search
class Luhn:
    def __init__(self, card_num):
        self.card_num = sub("[^0-9]","",card_num)
        self.can = search("[^0-9 ]",card_num)==None

    def valid(self):
        return (sum(int(i) for i in [*self.card_num[-1::-2]]) +sum((2*int(j)) if int(j) <5 else 2*int(j) -9 for j in [*self.card_num[-2::-2]]))%10 == 0 if len(self.card_num) > 1 and self.can else False

