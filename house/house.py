recite = lambda start_verse, end_verse: (
    []
    if end_verse - start_verse + 1 == 0
    else recite(start_verse, end_verse - 1)
    + [
        "This is the "
        + " ".join(
            [
                "horse and the hound and the horn that belonged to the",
                "farmer sowing his corn that kept the",
                "rooster that crowed in the morn that woke the",
                "priest all shaven and shorn that married the",
                "man all tattered and torn that kissed the",
                "maiden all forlorn that milked the",
                "cow with the crumpled horn that tossed the",
                "dog that worried the",
                "cat that killed the",
                "rat that ate the",
                "malt that lay in the",
                "house that Jack built.",
            ][-1 : -end_verse - 1 : -1][::-1]
        )
    ]
)
