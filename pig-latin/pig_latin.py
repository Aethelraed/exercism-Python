def translate(sentence):
    return " ".join(helper(word)for word in sentence.split())
    
def helper(word):
    '''
    1 - if word begins with vowel, xr or yt just add ay
    2 - if word has a qu then move that to back and add ay
    3 - if word has a y move all letters infront to the back and add ay
    4 - if word begins with other consonant move them to the back and add ay
    '''
    vowels = set("aeiou")
    #1
    if word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt":
        return word + "ay"
    #2
    if "qu" in word:
        return word[(word.index("u")+1):] + word[:(word.index("u")+1)] + "ay"     
    #4
    for i in range(len(word)):
        if word[i] in vowels and i > 0:
            return word[i:] + word[:i] + "ay"
    #3
    if "y" in word:
        return word[(word.index("y")):] + word[:(word.index("y"))] + "ay"


