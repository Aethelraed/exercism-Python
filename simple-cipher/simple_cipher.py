class Cipher:
    def __init__(self, key="aaaaaaaaaa"):
        self.letters = [*"abcdefghijklmnopqrstuvwxyz"]
        self.key = key

    def encode(self, text):
        return "".join([(self.letters[(self.letters.index(t)+self.letters.index(k))%len(self.letters)]) for t,k in zip(text,len(text)*self.key)])

    def decode(self, text):
        return "".join([(self.letters[(self.letters.index(t)-self.letters.index(k))%len(self.letters)]) for t,k in zip(text,len(text)*self.key)])
