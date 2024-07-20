def convert(number, a=""):
    if number % 3 == 0:
        a = a + "Pling"
    if number % 5 == 0:
        a = a + "Plang"
    if number % 7 == 0:
        a = a + "Plong"
    if not a:
        return str(number)
    return a
