import re


def count_words(sentence):
    words = re.sub(
        "^ |\.|\!|\?|:|\&|\@|\$|\%|\^|^'+|'+$",
        "",
        re.sub("  +|,|\t|\_", " ", re.sub("\n|,| +'+|'+ ", " ", sentence.lower())),
    ).split(" ")
    b = dict.fromkeys(sorted(set(words)))
    for w in words:
        b[w] = 1 if b[w] == None else b[w] + 1
    return b
