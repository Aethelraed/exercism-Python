def find(search_list, value, index=0):
    sll, pv = len(search_list), len(search_list) // 2 - 1
    if sll == 0 or value < search_list[0] or value > search_list[sll - 1]:
        raise ValueError("value not in array")
    return (
        index
        if value == search_list[0]
        else (
            index + sll - 1
            if value == search_list[sll - 1]
            else (
                find(search_list[:pv], value, pv)
                if value < search_list[pv]
                else find(search_list[pv:], value, index + pv)
            )
        )
    )
