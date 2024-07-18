def find_anagrams(word, candidates):
    return [c for c in candidates if (sorted(c.lower()) == sorted(word.lower()) and (word.lower() != c.lower()))]