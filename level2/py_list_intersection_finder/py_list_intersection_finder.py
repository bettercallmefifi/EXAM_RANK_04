def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    rst = []
    if len(lists) == 0:
        return rst

    for val in lists[0]:
        compteur = 0
        for liste in lists:
            if val in liste:
                compteur += 1
        if compteur == len(lists) and val not in rst:
            rst.append(val)
    return rst


def main():
    return print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))


if __name__ == "__main__":
    main()
