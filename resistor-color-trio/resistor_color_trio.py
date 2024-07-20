label = (
    lambda cols, colors=[
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]: str(
        str(
            10 ** colors.index(cols[2])
            * (10 * colors.index(cols[0]) + colors.index(cols[1]))
        )
        + " ohms"
    )
    .replace("000000000 ", " giga")
    .replace("000000 ", " mega")
    .replace("000 ", " kilo")
)
