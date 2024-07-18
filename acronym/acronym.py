def abbreviate(words):
    return "".join(i[0] for i in words.replace("-"," ").replace("_","").replace("   "," ").split(" ")).upper()
