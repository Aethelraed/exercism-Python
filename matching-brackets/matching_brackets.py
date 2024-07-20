def is_paired(
    input_string, brs=["[", "(", "{", None], brr=["]", ")", "}", None], stack=[None]
):
    for cs in tuple(input_string):
        if cs in brs:
            stack = stack + [cs]
        if cs in brr:
            if cs == brr[brs.index(stack[-1])]:
                stack = stack[:-1]
            else:
                return False
    return len(stack) == 1
