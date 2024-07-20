import re


def is_valid(isbn, helper=0):
    fu = tuple("".join(re.findall("[0,1,2,3,4,5,6,7,8,9,X]*", isbn)))
    if len(fu) != 10 or set(isbn) - set(tuple("1023456789X -")):
        return False
    for index, i in enumerate(fu):
        if i == "X" and index == 9:
            helper = helper + 10
        elif i == "X":
            print(i)
        else:
            helper = helper + int(i) * range(10, 0, -1)[index]
    return (helper % 11) == 0
