def resistor_label(cols):
    colors = [
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
    ]
    tols = {
        "grey": "0.05",
        "violet": "0.1",
        "blue": "0.25",
        "green": "0.5",
        "brown": "1",
        "red": "2",
        "gold": "5",
        "silver": "10",
    }
    if len(cols) == 1 and cols[0] == "black":
        return "0 ohms"
    band_three = str(colors.index(cols[-3])) if len(cols) == 5 else ""
    b1, b2, b3 = (
        str(
            str((10 * colors.index(cols[0]) + colors.index(cols[1])))
            + band_three
            + colors.index(cols[len(cols) - 2]) * "0"
            + " ohms"
            + " ±"
            + tols[cols[len(cols) - 1]]
            + "%"
        )
        .replace("000000000 ", " giga")
        .replace("000000 ", " mega")
        .replace("000 ", " kilo")
        .split(" ")
    )
    return (
        str(b1[-len(b1) : -3] + "." + b1[-3:].strip("0") + " " + b2)
        .replace("mega", "giga")
        .replace("kilo", "mega")
        .replace(" ohms", " kiloohms")
        + " "
        + b3
        if len(b1) > 3
        else " ".join([b1, b2, b3])
    )
