def flatten(iter):
    def helper(iter):
        for item in iter:
            try:
                yield from flatten(item)
            except TypeError:
                if item != None:
                    yield item

    return list(helper(iter))
