def sum_of_multiples(limit, multiples):
    helper = set()
    for mult in multiples:
        helper = helper | {i for i in range(limit) if mult > 0 and i % mult == 0}
    return sum(helper)
