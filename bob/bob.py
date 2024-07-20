def response(hey_bob):
    if len(hey_bob.strip(" \n\r\t")) < 1:
        return "Fine. Be that way!"
    if (hey_bob[-1] == "?") & (hey_bob.isupper()):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.strip(" \t")[-1] == "?":
        return "Sure."
    return "Whatever."
