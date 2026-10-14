def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    result = []
    if not lists:
        return []
    for value in lists[0]:
        compter = 0
        for liste in lists:
            if value in liste:
                compter += 1
        if compter == len(lists) and value not in result:
            result.append(value)
    return result


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
    print(list_intersection_finder([]))
    print(list_intersection_finder([[1, 2, 3], []]))
    print(list_intersection_finder([[5]]))