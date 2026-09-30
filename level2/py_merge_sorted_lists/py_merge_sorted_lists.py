def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    rst = []
    if not lists:
        return []
    for liste in lists:
        rst += liste

    i = 0
    while i < len(rst):
        j = i + 1
        while j < len(rst):
            if rst[i] > rst[j]:
                rst[i], rst[j] = rst[j], rst[i]
            j += 1
        i += 1

    return rst
~
