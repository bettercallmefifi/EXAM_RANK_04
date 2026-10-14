def palindrome(s) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return 0
    return 1

def palindrome_partitioner(s: str) -> int:
    if palindrome(s) == 1:
        return 0
    best = len(s) - 1
    for i  in range(1, len(s)):
        if palindrome(s[:i]) == 1:
            cuts = 1 + palindrome_partitioner(s[i:])
            if cuts < best:
                best = cuts
    return best