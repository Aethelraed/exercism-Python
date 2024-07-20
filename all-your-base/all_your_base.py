import math


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if len(digits) and (min(digits) < 0 or max(digits) >= input_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not sum(digits):
        return [0]
    help = 0
    out = []
    for index, dig in enumerate(digits):
        help = help + dig * input_base ** (len(digits) - index - 1)
    for i in range(math.ceil(math.log(help, output_base)), -1, -1):
        out = out + [help // (output_base**i)]
        help = help % (output_base**i)
    return out[not out[0] :]
