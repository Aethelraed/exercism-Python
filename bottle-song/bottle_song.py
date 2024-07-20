def recite(start, take=1):
    numbers = [
        "No",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
    ]
    single = lambda i: [
        f"{numbers[i]} green bottle{'' if i ==1 else 's'} hanging on the wall,",
        f"{numbers[i]} green bottle{'' if i ==1 else 's'} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        f"There'll be {numbers[i-1].lower()} green bottle{'' if i ==2 else 's'} hanging on the wall.",
    ] + ([""] if i > start - take + 1 and take > 1 else [])

    return sum([single(i) for i in range(start, start - take, -1)], [])
