def is_pangram(sentence, p =0):
    for i in set(sentence.upper()):
        p = p+ (i in set(tuple("abcdefghijklmnopqrstuvwxyz".upper().strip(" _"))))
    return p == 26