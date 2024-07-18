dt,td= list(tuple("abcdefghijklmnopqrstuvwxyz1234567890")),list(tuple("zyxwvutsrqponmlkjihgfedcba1234567890"))
def encode(plain_text):
    out,i = "",0
    for c in plain_text:
        if c in" .!?,": continue
        out,i=out+td[dt.index(c.lower())],i+1
        if i %5==0: out,i=out+" ", 0
    return out.strip(" ")


def decode(cipher):
    out = ""
    for c in "".join(cipher.split(" ")):
        out=out+dt[td.index(c.lower())]
    return out
