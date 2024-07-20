SUBLIST, SUPERLIST, EQUAL, UNEQUAL = "SUB", "SUP", "EQ", "NEQ"


def sublist(l1, l2):
    if l1 == l2:
        return EQUAL
    if any(l2[i : (i + len(l1))] == l1 for i in range(len(l2) - 1)):
        return SUBLIST
    if any(l1[i : (i + len(l2))] == l2 for i in range(len(l1) - 1)):
        return SUPERLIST
    return UNEQUAL
