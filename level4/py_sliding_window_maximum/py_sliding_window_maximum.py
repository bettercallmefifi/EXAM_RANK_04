def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    result = []
    if k <= 0:
        return []
    
    for i in range(len(nums) - k + 1):
        m = nums[i:]
        maximum = max(m[:k])
        result.append(maximum)
    return result

if __name__ == "__main__":
    print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sliding_window_maximum([1, 2, 3, 4, 5], 2))
    print(sliding_window_maximum([5, 4, 3, 2, 1], 1))
    print(sliding_window_maximum([1, 2, 3], 3))
    print(sliding_window_maximum([1, 2, 3], 4))
    print(sliding_window_maximum([], 2))
    print(sliding_window_maximum([1, 2, 3], 0))