numbers = [
    " || _ _  || ",
    "         || ",
    "  | ___  |  ",
    "    ___  || ",
    " |   _   || ",
    " |  ___   | ",
    " || ___   | ",
    "    _    || ",
    " || ___  || ",
    " |  ___  || ",
]  # 0-9


def ocr(string):
    # take a row of cells and ocr them into numbers
    # each cell consists of 4 lines and 3 columns
    # columns are joined at the end
    cells = [
        "".join(o) for o in list(zip(*string))
    ]  # linearize cell to reduce dimensions
    if len(cells[0]) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(cells) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    # if cell matches a number pattern append number else unrecognized character
    return "".join(
        [
            str(numbers.index(cell)) if cell in numbers else "?"
            for cell in [("".join(cells[i : i + 3])) for i in range(0, len(cells), 3)]
        ]
    )


def convert(string):
    # apply ocr to each row of cells
    i, rows = 0, []
    while i < len(string):
        # skip empty delimiter rows
        if string[i] == "         ":
            i += 1
        else:
            # append each row with numbers to rows to be processed
            rows.append(string[i : i + 4])
            i = i + 4
    return ",".join([ocr(cell) for cell in rows])
