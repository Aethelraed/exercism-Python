value = lambda cols, colors=[
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
]: 10 * colors.index(cols[0]) + colors.index(cols[1])
