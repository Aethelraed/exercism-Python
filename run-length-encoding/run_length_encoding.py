def decode(string):
    counter, out, helper = 1, "", 0
    for s in [*string]:
        if s in [*"1234567890"]:
            counter, helper = (
                10 * helper + int(s) if str(helper) in [*"1234567890"] else int(s)
            ), int(s)
        else:
            out, counter, helper = out + counter * s, 1, None
    return out


def encode(string):
    if len(string) == 0:
        return string
    current, counter, out = string[0], 0, ""
    for s in [*string] + ["_"]:
        if s == current:
            counter += 1
        else:
            out, counter, current = (
                out + (str(counter) if counter > 1 else "") + current,
                1,
                s,
            )
    return out
