def commands(bstr):
    ops, out = ["jump", "close your eyes", "double blink", "wink"], []
    rev, *com = bstr
    for c in range(len(com)):
        if com[c] == "1":
            out.append(ops[c])
    if rev == "0":
        out.reverse()
    return out
