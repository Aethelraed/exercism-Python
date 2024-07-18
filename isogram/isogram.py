is_isogram = lambda string: len(set("".join(("".join(string.upper().split(" "))).split("-")))) == len("".join(("".join(string.upper().split(" "))).split("-")))
