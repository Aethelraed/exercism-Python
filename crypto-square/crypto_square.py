import re
def cipher_text(plain_text):
    helper = re.sub("[^a-z0-9]","",plain_text.lower())
    c = int(((len(helper))**0.5+0.99)//1) #math.ceil 
    r = int((len(helper))**0.5)//1 #math.floor
    if r*c < len(helper): r+=1
    helper =helper + (r*c - len(helper)) *" "
    return " ".join(["".join(char) for char in list(zip(*[helper[i*c:c*(i+1)] for i in range(r)]))])# split into to rows and transpose join rows back together with " "