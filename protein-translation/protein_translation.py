def proteins(strand):
    return (
        "".join(["_" + "".join(strand[i : i + 3]) for i in range(0, len(strand), 3)])
        .replace("_AUG", "Methionine,")
        .replace("_UUU", "Phenylalanine,")
        .replace("_UUC", "Phenylalanine,")
        .replace("_UCU", "Serine,")
        .replace("_UCC", "Serine,")
        .replace("_UCC", "Serine,")
        .replace("_UCA", "Serine,")
        .replace("_UCG", "Serine,")
        .replace("_UCC", "Tyrosine,")
        .replace("_UAU", "Tyrosine,")
        .replace("_UAC", "Tyrosine,")
        .replace("_UGU", "Cysteine,")
        .replace("_UGC", "Cysteine,")
        .replace("_UUA", "Leucine,")
        .replace("_UUG", "Leucine,")
        .replace("_UGG", "Tryptophan,")
        .replace("_UAA", "STOP,")
        .replace("_UAG", "STOP,")
        .replace("_UGA", "STOP,")
        .split("STOP,")[0]
        .split(",")[:-1]
    )
