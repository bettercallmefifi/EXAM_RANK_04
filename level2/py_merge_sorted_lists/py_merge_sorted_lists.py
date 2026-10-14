def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = sum(lists, [])
    if not result:
        return []
    i = 0
    while i < len(result):
        j = i + 1
        while j < len(result):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
            j += 1
        i += 1
    return result

if __name__ == "__main__":
    print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
    print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
    print(merge_sorted_lists([[5], [1, 3], [2, 4]]))
    print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
    print(merge_sorted_lists([[], [1, 2, 3]]))
    print(merge_sorted_lists([[]]))
    print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
    print(merge_sorted_lists([[10], [10], [10]]))