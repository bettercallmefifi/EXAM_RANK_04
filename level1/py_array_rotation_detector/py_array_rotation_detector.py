def array_rotation_detector(arr1: list, arr2: list) -> bool:

    if not arr1 and not arr2:
        return True
    if len(arr1) == len(arr2):
        double = arr1 + arr1
        for i in range(len(arr1)):
            if double[i: i + len(arr1)] == arr2:
                return True
    return False

