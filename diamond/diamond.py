rows = lambda letter, spacer=" ", letters=[*"abcdefghijklmnopqrstuvwxyz".upper()]: [
    str(
        (letters.index(letter) - i) * spacer
        + letters[i]
        + (2 * i - 1) * spacer
        + letters[i]
        + (letters.index(letter) - i) * spacer
    ).replace("AA", "A")
    for i in [*range(letters.index(letter))] + [*range(letters.index(letter), -1, -1)]
]
