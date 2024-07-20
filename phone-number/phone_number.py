from re import sub, search


class PhoneNumber:
    def __init__(self, number):
        self.number = sub("\(| |\.|-|\)|\+", "", number)
        if search("[a-zA-Z]", self.number) != None:
            raise ValueError("letters not permitted")
        if search("[^0-9]", self.number) != None:
            raise ValueError("punctuations not permitted")
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(self.number) == 11 and not (self.number[0] == "1"):
            raise ValueError("11 digits must start with 1")
        if len(self.number) == 11:
            self.number = self.number[1:]
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        if self.exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")
        if self.area_code[0] in ["0"]:
            raise ValueError("area code cannot start with zero")
        if self.area_code[0] in ["1"]:
            raise ValueError("area code cannot start with one")

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.number[6:]}"
