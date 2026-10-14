def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if not arr1 and not arr2:
        return True
    if len(arr2) != len(arr1):
        return False
    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return False

if __name__ == "__main__":
    print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
    print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
    print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
    print(array_rotation_detector([1, 2], [1, 2, 3]))
    print(array_rotation_detector([], []))