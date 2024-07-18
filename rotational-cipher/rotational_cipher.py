def rotate(text, key):
    if key %26 ==0: return text
    cl = tuple("abcdefghijklmnopqrstuvwxyz")
    cu = tuple("abcdefghijklmnopqrstuvwxyz".upper())
    out = []
    for index,cr in enumerate(text):
        if cr in cl: out.append(cl[(cl.index(cr)+key)%26])
        elif cr in cu: out.append(cu[(cu.index(cr)+key)%26])
        else: out.append(cr)
    return "".join(out)
        