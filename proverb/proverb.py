def proverb(*inputs, qualifier):
    if not inputs:
        return []
    out, qu = [], ""
    if qualifier:
        qu = qualifier + " "
    for i in range(0, len(inputs) - 1):
        out = out + [
            "For want of a " + inputs[i] + " the " + inputs[i + 1] + " was lost."
        ]
    return out + ["And all for the want of a " + qu + inputs[0] + "."]
