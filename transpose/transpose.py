def transpose(a):
    return "\n".join(
        [
            "".join(x).rstrip("*")
            for x in zip(
                *[x.ljust(len(max(a.split("\n"), key=len)), "*") for x in a.split("\n")]
            )
        ]
    ).replace("*", " ")
