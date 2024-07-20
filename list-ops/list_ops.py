def append(list1, list2):
    return [*list1, *list2]


def concat(lists):
    return foldl(append, lists, [])


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    return sum(1 for l in list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    return (
        initial if not list else foldl(function, list[1:], function(initial, list[0]))
    )


def foldr(function, list, initial):
    return foldl(function, list[::-1], initial)


def reverse(list):
    return list[::-1]
