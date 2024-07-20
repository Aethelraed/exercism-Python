def recite(start_verse, end_verse):
    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]
    presents = [
        "and a Partridge in a Pear Tree",
        "two Turtle Doves,",
        "three French Hens,",
        "four Calling Birds,",
        "five Gold Rings,",
        "six Geese-a-Laying,",
        "seven Swans-a-Swimming,",
        "eight Maids-a-Milking,",
        "nine Ladies Dancing,",
        "ten Lords-a-Leaping,",
        "eleven Pipers Piping,",
        "twelve Drummers Drumming,",
    ]
    p_string = (
        " ".join(presents[end_verse - 1 :: -1])
        if end_verse > 1
        else presents[0].replace("and ", "")
    )
    return (
        recite(start_verse, end_verse - 1)
        + [
            f"On the {days[end_verse-1]} day of Christmas my true love gave to me: {p_string}."
        ]
        if end_verse - start_verse >= 0
        else []
    )
